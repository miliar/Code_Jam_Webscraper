#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<math.h>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include<string>

typedef unsigned long long ull;

using namespace std;

ull calc(ull base,string coin){
    ull ans=0;
    ull digit=0;
    for(int i=coin.length()-1;i>=0;i--){
        ans += pow(base, digit++) * (coin[i]-'0');
    }
    return ans;
}

ull getDivisor(ull num){
    ull square_root = (ull) sqrt(num) + 1;
    for (ull i = 2; i < square_root; i++){
        if (num % i == 0 && i!=num)
            return i;
    }
    return -1;
}

string getBinary(ull i,int bit){
    string str;
    while(i){
        str.push_back(i%2 + '0');
        i/=2;
    }
    while(str.length()!=bit){
        str.push_back('0');
    }
    reverse(str.begin(), str.end());
    return str;
}

int main()
{
    freopen("/Users/shitian/Desktop/programmingcCntest/GCJ/gcj/gcj/C-small-attempt0.in", "r", stdin);
    freopen("/Users/shitian/Desktop/programmingcCntest/GCJ/gcj/gcj/out.txt", "w", stdout);
//

    int tcase;
    cin>>tcase;
    for(int tca=1;tca<=tcase;tca++){
        cout<<"Case #"<<tca<<":"<<endl;
        
        int n,j;
        cin>>n>>j;
        int count=0;
        for(ull coin=((1<<(n-1))+1);coin<(1<<n)-1;coin+=2){
            string binary = getBinary(coin,n);
            //cout<<binary<<endl;
            vector<ull>vec;
            for(int base=2;base<=10;base++){
                ull now = calc(base,binary);
                
                //cout<<now<<endl;
                ull div = getDivisor(now);
                if(div == -1){
                    goto next;
                }
                vec.push_back(div);
            }
            cout<<getBinary(coin,n)<<" ";
            for(int i=0;i<vec.size()-1;i++){
                cout<<vec[i]<<" ";
            }
            cout<<vec[vec.size()-1]<<endl;
            count ++;
            if(count == j){
                break;
            }
        next:;
        }
    }
  
    return 0;
}