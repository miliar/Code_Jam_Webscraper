/*
 *Aditya Gourav @ adi.pearl
 */
#include<bits/stdc++.h>
using namespace std;

#define R(f) freopen(f,"r",stdin);
#define W(f) freopen(f,"w",stdout);
#define TEST int num_cases; cin>>num_cases;for(int case_id=1;case_id <= num_cases;++case_id)

typedef unsigned long long ull;

/** Main Code starts here :) **/
#define SUBMIT
int main(){
    #ifdef SUBMIT
    R("A-large.in");
    W("A-large.txt");
    #endif

    TEST{

        int n;
        cin >> n;

        printf("Case #%d: ", case_id);

        if(n == 0){
            printf("INSOMNIA\n");
            continue;
        }

        int a = 0;
        ull x = n;
        while(a != 0x3ff){
            ull y = x;
            while(y){
                a |= (1<<(y%10));
                y /= 10;
            }
           x += n;
        }
        x -= n;

        cout << x << endl;
        //db("CASE ",case_id);



    }

    return 0;
}
