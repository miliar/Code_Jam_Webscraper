#include <bits/stdc++.h>

using namespace std;

#define ll long long

string arr[113];

int main() {
	// your code goes here
    int t,i,k,j,flag;string ss,temp;
    cin>>t;
    for(int g=1;g<=t;g++){
        k=0,flag=0;
        cin>>ss;
        arr[k++]=ss[0];
        for(i=1;i<ss.length();i++){
                temp=ss[i];
                if(temp.compare(arr[k-1])){
                    arr[k++]=ss[i];
                }
            }

            // whatch

            /*for(int h=0;h<k;h++)
                cout<<arr[h];*/

        for(i=k-1;i>=0;i--){
            temp=arr[i];
            if(temp.compare("-")==0){
                cout<<"Case #"<<g<<": "<<i+1<<endl;
                flag=1;
                break;
            }

        }
        if(flag==0)
            cout<<"Case #"<<g<<": "<<0<<endl;

        }

    
	
	return 0;
}