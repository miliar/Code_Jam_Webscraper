#include<bits/stdc++.h>
using namespace std;

template <typename T>
  string NumberToString ( T Number )
  {
     ostringstream ss;
     ss << Number;
     return ss.str();
  }
int main(){

    ofstream out;
    ifstream in;
    out.open("LargeOut.txt");
    in.open("A-large.in");
    int t;
    in>>t;
    for(int i=0;i<t;i++){
        long int n,temp;
        bool ints[10]={false};
        in>>n;
        temp=n;

        for(int i=1;;i++){
            if(n==0)break;
            temp=i*n;
            string s=NumberToString(temp);

            for(int i=0;i<10;i++){
                if(ints[i]==false){
                    if(s.find('0'+i)!=string::npos){
                        ints[i]=true;//cout<<"i##"<<i<<endl;
                    }
                }
            }
            int sum = std::accumulate(ints, ints + 10, 0);
            if(sum == 10)break;
        }
        int sum = std::accumulate(ints, ints + 10, 0);
        if(sum==10){
            out<<"Case #"<<i+1<<": "<<temp<<endl;
        }

        if(n==0){
            out<<"Case #"<<i+1<<": INSOMNIA"<<endl;
        }
    }
    return 0;
}
