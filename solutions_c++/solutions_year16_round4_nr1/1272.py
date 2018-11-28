#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cassert>

using namespace std;

template<typename T>
vector<vector<T>> get_all_subsets(vector<T> base)
{
   if (base.empty()) {
      return {{}};
   }

   auto last_element = base.back();
   base.pop_back();

   auto all_remaining_subsets = get_all_subsets(base);

   vector<vector<T>> all_subsets;

   for (auto& subset : all_remaining_subsets) {
      all_subsets.push_back(subset);
      subset.push_back(last_element);
      all_subsets.push_back(subset);
   }

   return all_subsets;
}

template<typename T>
vector<vector<T>> get_all_subsets_with_fixed_num_elements(vector<T> base, size_t k)
{
   assert(base.size() >= k);

   if (base.size() == k) {
      return {base};
   }

   if (k == 0) {
      return {{}};
   }

   auto last_element = base.back();
   base.pop_back();

   vector<vector<T>> all_subsets;

   // pick last_element
   for (auto& subset : get_all_subsets_with_fixed_num_elements(base, k - 1)) {
      subset.push_back(last_element);
      all_subsets.push_back(subset);
   }

   // don't pick last_element
   for (auto& subset : get_all_subsets_with_fixed_num_elements(base, k)) {
      all_subsets.push_back(subset);
   }

   return all_subsets;
}

template<typename T>
vector<vector<T>> get_all_subsets_with_at_most_num_elements(vector<T> base, size_t k)
{
   if (k == 0 or base.empty()) {
      return {{}};
   }

   auto last_element = base.back();
   base.pop_back();

   vector<vector<T>> all_subsets;

   // pick last_element
   for (auto& subset : get_all_subsets_with_at_most_num_elements(base, k - 1)) {
      subset.push_back(last_element);
      all_subsets.push_back(subset);
   }

   // don't pick last_element
   for (auto& subset : get_all_subsets_with_at_most_num_elements(base, k)) {
      all_subsets.push_back(subset);
   }

   return all_subsets;
}

vector<int> to_binary(long long num)
{
   if (num == 0) {
      return {0};
   }
   else if (num == 1) {
      return {1};
   }

   long long new_num = num;
   if (new_num % 2 == 1) {
      auto vec = to_binary((num - 1) / 2);
      vec.push_back(1);
      return vec;
   }
   else {
      auto vec = to_binary(num / 2);
      vec.push_back(0);
      return vec;
   }
}

vector<int> to_length_k_binary(long long num, size_t k) {
   auto vec = to_binary(num);
   vector<int> zeros;
   for (size_t i = 0; i < k - vec.size(); i++) {
      zeros.push_back(0);
   }

   zeros.insert(zeros.end(), vec.begin(), vec.end());
   return zeros;
}

class ProblemSolver {
public:
   ProblemSolver(istream& in, ostream& out) :
      in(in),
      out(out) { }

   void solve()
   {
      int T;
      in >> T;

      for (int t = 1; t <= T; t++) {
         solve_case(t);
      }
   }

private:
   void solve_case(int t);

   istream& in;
   ostream& out;
};

struct Triple {
   int N;
   int R, P, S;

   int A() {
      return (R + P + S)/3;
   }

   bool possible() {
      assert (P + R + S == pow(2, N));
      return abs(R - P) > 1 or abs(P - S) > 1 or abs(S - R) > 1 ? false : true;
   }

   pair<Triple, Triple> get_both() {
      int a = A();
      if (N % 2 == 1) {
         if (S < P and S < R) {
            return {{N - 1, a/2, a/2 +1, a/2}, {N - 1, a/2 +1, a/2, a/2}};
         }
         else if (P < R and P < S) {
            return {{N - 1, a/2 + 1, a/2, a/2}, {N - 1, a/2, a/2, a/2 + 1}};
         }
         else {
            return {{N - 1, a/2, a/2 + 1, a/2}, {N - 1, a/2, a/2, a/2  + 1}};
         }
      }
      else {
         if (S > R and S > P) {
            return {{N - 1, a/2, a/2 + 1, a/2 + 1}, {N - 1, a/2 + 1, a/2, a/2 + 1}};
         }
         else if (P > R and P > S) {
            return {{N - 1, a/2 + 1, a/2 + 1, a/2}, {N - 1, a/2, a/2 + 1, a/2 + 1}};
         }
         else {
            return {{N - 1, a/2 + 1, a/2 + 1, a/2}, {N - 1, a/2 + 1, a/2, a/2 + 1}};
         }
      }
   }

   string to_string() {
      if (not possible()) {
         return "IMPOSSIBLE";
      }

      if (N == 0) {
         if (S == 1) {
            return "S";
         }
         else if (P == 1) {
            return "P";
         }
         else {
            return "R";
         }
      }

      auto both = get_both();

      return both.first.to_string() + both.second.to_string();
   }
};

void ProblemSolver::solve_case(int t)
{
   out << "Case #" << t << ": ";

   Triple triple;
   in >> triple.N >> triple.R >> triple.P >> triple.S;

   out << triple.to_string() << endl;
}


int main()
{
//   istream& in = cin;
   ifstream in;
//   in.open("../instances/A-small-attempt0.in");
   in.open("../instances/A-large.in");

//   ostream& out = cout;
   ofstream out;
//   out.open("../results/A-small.out");
   out.open("../results/A-large.out");

   if (not in) {
      cout << "could not open file!" << endl;
      return 1;
   }

   ProblemSolver solver{in, out};
   solver.solve();

   return 0;
}

