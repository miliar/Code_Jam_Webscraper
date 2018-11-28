#include <bits/stdc++.h>
using namespace std;


int main(){
    freopen("A-large.in","r",stdin);
    freopen("on.c","w",stdout);

    int tc , n , number_case = 1;
    cin >> tc;

    while(tc--){
        cin >> n;


        set<int> s;
        int current = n;
        while(current > 0){
            int tmp = current;
            while(tmp > 0){
                s.insert(tmp%10);
                tmp/=10;
            }
            if(s.size() == 10){
                break;
            }
            current += n;
        }
        printf("Case #%d: ",number_case++);
        if(s.size() == 10){
            printf("%d\n",current);
        }else{
            printf("INSOMNIA\n");
        }


    }





    return 0;
}
