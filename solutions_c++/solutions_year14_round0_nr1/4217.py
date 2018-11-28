#include<cstdio>
#include<iostream>
#include<cstring>
#include<cmath>
#include<vector>
#include<map>

using namespace std;
#define getcx getchar_unlocked
#define scani(i) scanf("%d",&i)
#define scanl(i) scanf("%lld",&i)
#define LL long long
#define PB push_back
#define MP make_pair

int main(){
    int t;
    cin>>t;
    for(int i=0;i<t;i++){
        int mat[4],temp,ans,cnt=0,r;
        cin>>r;
        for(int j=0;j<4;j++){
            for(int k=0;k<4;k++){
                cin>>temp;
                if(j+1==r)  mat[k]=temp;
            }
        }
        cin>>r;
        for(int j=0;j<4;j++){
            for(int k=0;k<4;k++){
                cin>>temp;
                if(j+1==r){
                    for(int m=0;m<4;m++){
                        if(mat[m]==temp){
                            ans=temp;
                            cnt++;
                        }
                    }
                }
            }
        }
        if(cnt==1)
            cout<<"Case #"<<i+1<<": "<<ans<<"\n";
        else if(cnt==0)
            cout<<"Case #"<<i+1<<": Volunteer cheated!\n";
        else
            cout<<"Case #"<<i+1<<": Bad magician!\n";
    }
    return 0;
}
