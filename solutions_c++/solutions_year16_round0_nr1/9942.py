#include<bits/stdc++.h>

using namespace std;

int main(){
    int T;
    scanf("%d",&T);

    unsigned long long int temp, recover, last;
    int i = 0;
    while(i < T){
        int N;
        scanf("%d",&N);
        set<int> numbers;
        if( N > 0){
            //cout << "caso "<< N << endl;
            for(int j = 1; numbers.size() < 10; j++ ){
/*
                cout << "newFor " << N << endl;
                for (set<int>::iterator it=numbers.begin(); it!=numbers.end(); ++it)
                    cout << ' ' << *it;
                cout << '\n';*/

                recover = N*j;
                last = recover;
                for( int k = 0; recover > 0; k++ ){
                    temp = recover%10;
                    recover/=10;
                    numbers.insert(temp);
                }

            }
            printf("Case #%d: %I64u\n",i+1,last);
        }else
            printf("Case #%d: INSOMNIA\n",i+1);

        i++;
    }




}
