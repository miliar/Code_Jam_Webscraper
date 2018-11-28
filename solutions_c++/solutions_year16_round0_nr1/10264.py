#include <iostream>
#include <cstdio>
#include <map>

using namespace std;

inline string IntToString(int a){
    char x[100];
    sprintf(x,"%d",a); string s = x;
    return s;
}

bool cek(map<int,bool> data){
    return data[0]==true && data[1]==true && data[2]==true && data[3]==true && data[4]==true && data[5]==true && data[6]==true && data[7]==true && data[8]==true && data[9]==true;
}

int main(){

    freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
    int T;
    cin>>T;


    for(int i=1;i<=T;i++){
        cout<<"Case #"<<i<<": ";
        map<int,bool> data;
        long long int N;
        cin>>N;
        int counter=0;
        if(N==0){
            cout<<"INSOMNIA"<<endl;
        }
        else{
            int j=1;
            int M;
            while(!cek(data)){
                counter++;
                 M = N*j;
                string str = IntToString(M);
                for(int i=0;i<str.size();i++){
                        int res;
                        char x[1];
                        x[0] = str[i];
                        sscanf(x,"%d",&res);
                        data[res] = true;
                }
                j++;
            }
                    cout<<M<<endl;
        }


    }

  return 0;

}
