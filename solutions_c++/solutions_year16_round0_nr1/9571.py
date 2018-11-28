#include<iostream>
#include<fstream>
using namespace std;

long long fxn(long long vl){
    if(vl == 0)
        return -1;
    long long arr[10];
    for(int index =0; index < 10; index++)
                            arr[index] = 0;
    long long n = vl;
    long long no = n,pre = 0;
    for(int index = 0; ; index++){
        no = n;
        while(no){
            if(arr[(no%10)] == 0){
                pre++;
                arr[(no%10)] = 1;
            }

            no /= 10;
        }
        if(pre == 10){
            return n;
        }
        n += vl;
    }
}
int main(){
    int tc;

    ifstream inputfile("A-large.in");
    ofstream outputfile("output.txt");
    inputfile>>tc;
    long long val;
    for(int index = 1; index <= tc; index++){
        inputfile>>val;
   //     cout<<val<<": ";
        val = fxn(val);
     //   cout<<val<<endl;
        if(val == -1)
          outputfile<<"Case #"<<index<<": INSOMNIA"<<endl;
        else
          outputfile<<"Case #"<<index<<": "<<val<<endl;
    }
    inputfile.close();
    outputfile.close();
    return 0;
}
