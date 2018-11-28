#include<iostream>
#include<fstream>

using namespace std;

int main(){
    ifstream cin("A-large.in");
    ofstream cout("A-large.out");
    int T;

    cin>>T;

    for(int i=0;i<T;i++){
        int nShy;
        cin>>nShy;

        int arr[nShy+1];
        for(int k=0;k<=nShy;k++)arr[k]=0;
        //cout<<" _ array _ "<<" -  ";
       // for(int x=0;x<=nShy;x++)cout<< arr[x];


        int ccount=0;
        string shys;
        cin>>shys;

        arr[0]=shys[0]-'0';

        for(int f=1;f<=nShy;f++){
             int temp=0;

            if(f>(arr[f-1]))
            temp+=f-(arr[f-1]);

            ccount+=temp;

          //  cout<<"\n temp count "<<temp<<" [ " <<(shys[f-1]-'0')<<endl;
            arr[f]=arr[f-1]+(shys[f]-'0')+temp;

           // cout<<" _ array _ "<<" -  ";
        //   for(int x=0;x<=nShy;x++)cout<< arr[x];

        }
        cout<<"Case #"<<i+1<<": "<<ccount<<endl;



    }



}
