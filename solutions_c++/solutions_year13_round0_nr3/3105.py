#include<iostream>
#include<stdio.h>
#include<string>
#include<sstream>
#include<vector>

using namespace std;

bool is_palin(long long i){
    string x = static_cast<ostringstream*>( &(ostringstream() << i) )->str();
    string y = "";
 //   cout << i ;
    while(i > 0){
        y += 48+i%10;
        i/=10;
    }
//cout <<  "   " << y << endl;
    return (x.compare(y) == 0)? true: false;
}
int arr[11]={0};
vector<int> v;
void palin(int pos, int len){
    if(pos >= len){
        // push palindrome creoatd
        int n = 0;
        for(int i=0; i < len ; i++){
            n = n*10 + arr[i];
        }
        if(n !=0)
            v.push_back(n);
        //cout << n << endl;
        return;
    }
    if(pos < len/2){
        for(int i=0;i<=9;i++){
            if(i==0 && pos == 0) continue;
            arr[pos]=i;
            palin(pos+1,len);
        }
    } else if( pos > len/2){
        arr[pos] = arr[len - pos -1];
        palin(pos+1, len);
    } else {
        if( len % 2 == 0){
            arr[pos] = arr[len - pos -1];
            palin(pos+1, len);
        } else {
            for(int i=0;i<=9;i++){
                arr[pos] = i;
                palin(pos+1,len);
            }
        }
    }
        
}
int main(){
    int a[1000000] = {0};
    int c=0;
    //for(int i=0;i<10000000;i++){
    //    if(is_palin(i))
    //        a[c++] = i;
    //}
//cout <<  c << endl;
    for(int i=1;i<=7;i++){
        palin(0,i);
    }
//    cout << v.size() << endl;
    vector<long long> ans;
    for(int i=0;i<v.size();i++){
        long long tmp = v[i] * v[i];
        if( is_palin(tmp)) 
            ans.push_back(tmp);

    }
    int cases;
    scanf("%d",&cases);
    for(int c=1;c<=cases;c++){
        long long a,b;
        scanf("%lld %lld", &a,&b);
        int res = 0;
        for(int i=0;i<ans.size();i++){
           if( a<= ans[i] && ans[i] <= b)
               res++;
        }
        printf("Case #%d: %d\n",c,res);
    }

}
