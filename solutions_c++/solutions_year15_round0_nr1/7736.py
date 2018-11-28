#include<iostream>
#include<string>
using namespace std;

int main(){
    int tc,res=0,j,res1,dif;
    string s;
    cin>>tc;
    int i  , len;
    for(i=0;i<tc;i++){
        res=0;
        cin>>len;
        cin>>s;
        int arr[len+1];
        for(j=0;j<=len;j++){
            arr[j]=(int)s[j]-48;

        }
        res1=0;
        int fin=0;
        //for(j=0;j<=len;j++)
            //cout<<arr[j]<<" ";

        for(j=1;j<=len;j++){
            res1+=arr[j-1];
            if(res1<j){
                dif=j-res1;
                fin+=dif;
                res1+=dif;
            }
        }
        cout<<"Case #"<<i+1<<":"<<" "<<fin;
        cout<<endl;





    }


}
