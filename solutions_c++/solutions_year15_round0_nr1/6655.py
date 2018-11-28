#include <iostream>

using namespace std;

int main()
{
    int t,s,stand,extra,i,a[10005],k,temp;
    char b[10005];
    cin>>t;
    k=1;
    while(t--){
        extra=0;
        stand=0;
        cin>>s;
       // cout<<"after s"<<endl;
 //      cin>>s
//        cin>>temp;
//        i=0;
//        while(temp!=0){
//            a[i]=temp%10;
//            temp=temp/10;
//            i++;
//
//        }
        cin>>b;
        for(int i=0;i<s+1;i++){
            a[i]=b[i]-48;


        }
       // cout<<"now:"<<endl;
       // for(int i=0;i<s+1;i++)cout<<a[i]<<" ";
        // cout<<"after assignment"<<endl;
        for(int i=0;i<s+1;i++){
          //   cout<<"in first loop"<<endl;
            if(stand>=i)stand=stand+a[i];
            else if(a[i]!=0){
                extra+=i-stand;
                stand+=i-stand+a[i];
            }
        }
       // cout<<"stand:"<<stand<<endl;
        //cout<<"extra:"<<extra<<endl;
        cout<<"Case #"<<k<<": "<<extra<<endl;
        k++;

    }
    return 0;
}
