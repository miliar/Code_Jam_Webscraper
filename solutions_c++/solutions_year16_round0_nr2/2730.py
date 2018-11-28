// C++ 11 code
#include <iostream>
#include <algorithm>

using namespace std;

const int INF=10000;

int count_num_plus_minus(string S){

    int num = 0;

    for(int i=0; i<S.size()-1; i++){

        if(S[i] == '+' && S[i+1] == '-') num++;

    }

    return num;
}


int solve_greedy(string S){

    int ans = 2*count_num_plus_minus(S);

    if(S[0] == '-') ans++;

    return ans;

}


/**
 * @brief is_uniform
 * @param S
 * @return 1 if the string contain only +, 2 if the string contains only -, 0 otherwise
 */
int is_uniform(string S){

    auto num_plus = count(S.begin(), S.end(), '+');

    if(num_plus == S.size()) return 1;
    else if(num_plus == 0) return 2;
    return 0;

}

string remove_trailing_plus(string S){

    int pos = 0;

    for(int i=0; i<S.size(); i++){
        if(S[i] == '-') pos = i+1;
    }

    return S.substr(0, pos);
}


string maneuver(string S, int pos){

    for(int i=0; i<= pos; i++){

        if(S[i] == '+') S[i] = '-';
        else S[i] = '+';
    }

    reverse(S.begin(), S.begin()+pos+1);

    return S;
}


void solve_brute_force(string S, int pos, int num_changes, int& current_solution){

    int tmp = is_uniform(S);

    if(tmp){
        current_solution = min(num_changes + tmp - 1, current_solution);
        //return num_changes + tmp - 1;
        return;
    }

    if(num_changes + 1 >= current_solution){

        //return INF;
        return;
    }

    string ss = remove_trailing_plus(S);


    for(int i=0; i<ss.size(); i++){

        if(i != pos){

            string sss = maneuver(ss, i);

            solve_brute_force(sss, i, num_changes+1, current_solution);

        }
    }


}

bool comp_plus_minus(char& l, char& r){
     return l<r;
}

void test_all(int n){

    int num_test = 0;
    int num_same = 0;
    int num_better = 0;
    int num_worse = 0;

    for(int i=1; i<=n; i++){

        for(int j=0; j<=i; j++){

            string s(i, '-');
            for(int k=0; k<j; k++){

                s[k] = '+';
            }

            sort(s.begin(), s.end());

            do{

                int max_num_changes = solve_greedy(s);
                num_test++;
                cout<<"Processing "<<num_test<<endl;
                int brute_answer = max_num_changes+2;

                solve_brute_force(s, -1, 0, brute_answer);

                int ans = brute_answer;

                if(ans == max_num_changes) num_same++;
                if(ans < max_num_changes) num_better++;
                if(ans > max_num_changes) num_worse++;



            }while(next_permutation(s.begin(), s.end()));






        }
    }

    cout<<"num_test: "<<num_test<<" num_better: "<<num_better<<" num_worse: "<<num_worse<<" num_same: "<<num_same<<endl;

}

void test_one(vector<string> ss){

    int num_test = 0;
    int num_same = 0;
    int num_better = 0;
    int num_worse = 0;

    for(auto s:ss){

        int max_num_changes = solve_greedy(s);
        num_test++;
        cout<<"Processing "<<num_test<<endl;
        int brute_answer = max_num_changes+2;

        solve_brute_force(s, -1, 0, brute_answer);

        int ans = brute_answer;

        if(ans == max_num_changes) num_same++;
        if(ans < max_num_changes) num_better++;
        if(ans > max_num_changes) num_worse++;
    }

    cout<<"num_test: "<<num_test<<" num_better: "<<num_better<<" num_worse: "<<num_worse<<" num_same: "<<num_same<<endl;



}

void test_sample(){

    int T;
    cin>>T;
    string S;

    for(int c=1; c<=T; c++){

        cin>>S;

        cout<<"Case #"<<c<<": "<<solve_greedy(S)<<endl;
    }
}

int main()
{
    test_sample();
    //test_all(9);
    //test_one({"+++---+++-----", "+-+-", "+-+-+-+-+-+-"});
    return 0;
}

