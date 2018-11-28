#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<string>
using namespace std;
//1,i,j,k
//1,2,3.4
int mul(int i,int j){
    if(i==1)return j;
    if(j==1)return i;
    int flag=1;
    if(i*j<0)flag=-1;
    if(i<0)i*=-1;
    if(j<0)j*=-1;

    if(i==2){
        if(j==2)return -1*flag;
        if(j==3)return 4*flag;
        if(j==4)return -3*flag;
    }
    if(i==3){
        if(j==2)return -4*flag;
        if(j==3)return -1*flag;
        if(j==4)return 2*flag;
    }
    if(i==4){
        if(j==2)return 3*flag;
        if(j==3)return -2*flag;
        if(j==4)return -1*flag;
    }
}

int remul(int i,int j){
    int flag=1;
    if(i*j<0)flag=-1;
    if(i<0)i*=-1;
    if(j<0)j*=-1;

    if(i==1){
        if(j==1)return 1*flag;
        if(j==2)return -2*flag;
        if(j==3)return -3*flag;
        if(j==4)return -4*flag;
    }
    if(i==2){
        if(j==1)return 2*flag;
        if(j==2)return 1*flag;
        if(j==3)return 4*flag;
        if(j==4)return -3*flag;
    }
    if(i==3){
        if(j==1)return 3*flag;
        if(j==2)return -4*flag;
        if(j==3)return 1*flag;
        if(j==4)return 2*flag;
    }
    if(i==4){
        if(j==1)return 4*flag;
        if(j==2)return 3*flag;
        if(j==3)return -2*flag;
        if(j==4)return 1*flag;
    }
}

int toForm(char c){
    if(c=='i')return 2;
    if(c=='j')return 3;
    if(c=='k')return 4;
}
bool isComple(string str,int start,int len,int taget){
    if(taget==5){
        return len==start;
    }
    if(len<=start)return false;
    if(taget==4){
        int now=1;
        for(int i=start;i<len;i++){
            int curr=toForm(str[i%str.length()]);
            now=mul(now,curr);
        }
        if(now!=4)return false;
    }
    int now=1;
    bool falg=false;
    while(start<len){
        int curr=toForm(str[start%str.length()]);
        now=mul(now,curr);
        if(now==taget){
            falg|=isComple(str,start+1,len,taget+1);
        }
        if(falg)return true;
        start++;
    }
    return falg;
}
int ans[10000005];
int main(){
    int t;
    cin>>t;
    for(int cas=1;cas<=t;cas++){
        int l,x;
        cin>>l>>x;
        string str;
        cin>>str;
        int len=str.length()*x;
        ans[0]=1;
        for(int i=1;i<=len;i++){
            int curr=toForm(str[(i-1)%str.length()]);
            ans[i]=mul(ans[i-1],curr);
           // cout<<ans[i]<<" ";
        }
        //cout<<endl;
        bool falg=false;
        for(int i=1;i<=len;i++){
            if(ans[i]==2){
                for(int j=i+1;j<=len;j++){
                    //cout<<remul(ans[j],ans[j-1])<<" v "<<remul(ans[len],ans[j])<<endl;
                    if(remul(ans[j],ans[i])==3&&remul(ans[len],ans[j])==4){
                        falg=true;
                        break;
                    }
                }
            }
            if(falg)break;
        }
        if(falg){
            cout<<"Case #"<<cas<<": YES"<<endl;
        }
        else{
            cout<<"Case #"<<cas<<": NO"<<endl;
        }
    }
}
