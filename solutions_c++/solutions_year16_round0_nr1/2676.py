#include <iostream>
#include <vector>

using namespace std;

typedef long long int lli;



vector<int> get_digits(lli N){

    vector<int> digits;

    while(N){

        digits.push_back(N%10);
        N /= 10;
    }

    return digits;

}

bool is_solution(vector<bool> is_digits){

    int num_digits = 0;

    for(int i=0; i<is_digits.size(); i++){

        num_digits += is_digits[i];
    }


    return num_digits == 10;
}

int solve_bruteforce(lli N){

    if(N == 0) return -1;

    lli factor = 1;

    vector<bool> is_digits(10, false);

    while(true){

        auto digits = get_digits(N*factor);

        for(auto digit: digits){

            is_digits[digit] = true;
        }

        if(is_solution(is_digits)) return N*factor;

        factor++;

    }

}

void test_all(){

    for(lli i=0; i<=1e6;i++){

        cout<<"Processing "<<i<<endl;

        solve_bruteforce(i);
    }


}

void test_sample(){

    int T;
    cin>>T;
    int N;

    for(int c=1; c<=T; c++){

        cin>>N;

        auto ans = solve_bruteforce(N);

        cout<<"Case #"<<c<<": ";


        if(ans == -1){
            cout<<"INSOMNIA"<<endl;
        } else{
            cout<<ans<<endl;
        }


    }
}


int main()
{
    //test_all();
    test_sample();
    return 0;
}

