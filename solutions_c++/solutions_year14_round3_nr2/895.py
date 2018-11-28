#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

bool is_valid(vector<string> v, int A[])
{
  string s="";
  for (int i=0; i<v.size(); i++) {
    s+=v[A[i]];
  }

  int freq[26] = {0};
  for (int i=0; i<s.length(); i++){
    freq[s[i]-'a']++;
  }

  int i =0;
  while(i<s.length())  {
    for (int j=i; j<i+freq[s[i]-'a']; j++) 
      if (s[j] != s[i]) { 
        return false;
      }
    int tmp = s[i] - 'a';
    i += freq[tmp];
  }

  return true;
}

void swap(string& s1, string& s2)
{
  string tmp = s1;
  s1 = s2;
  s2 = s1;
}

void swap(int* a, int *b)
{
int tmp = *a;
*a = *b;
*b = tmp;
}

int permute(const vector<string>& in, int index, int A[])
{
  if (index == in.size()) {
    if(is_valid(in, A)) return 1;
    else return 0;
  }

  int res = 0;
  for (int i=index; i<in.size(); i++) {
    swap(&A[index], &A[i]);
    res += permute(in, index+1, A);
    swap(&A[index], &A[i]);
  }

  return res;
}

int main()
{
  int n_cases;
  ifstream file("B.in", ios::in);

  file >> n_cases;
  
  for (int case_no=1; case_no <= n_cases; case_no++) {
    int N;
    file >> N;

    vector<string> in, out;
    string s;
    int A[N];
    for (int i=0;i<N;i++) { file >> s; in.push_back(s);A[i]=i; }

    int ret = permute(in, 0, A);

    cout << "Case #" << case_no << ": " << ret << endl;
  }
}
