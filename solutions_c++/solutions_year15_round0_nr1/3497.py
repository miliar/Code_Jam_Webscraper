#include<iostream>
#include<fstream>

using namespace std;


int main(){
    ifstream  fin("/Users/anupsing/Desktop/GCJ/input.txt");
    ofstream  fout("/Users/anupsing/Desktop/GCJ/output.txt");
    int T;
    string str;

    fin>>T;
    int cases=1;
    while(T--) {

        int len;
        fin>>len;
        fin>>str;

        int tot=0;
        int ans=0;

                tot+=str[0]-'0';
              //  cout<<"tot "<<tot<<endl;
                for(int i=1;i<=len;i++){
                    if(str[i]>'0') {
                        if(tot<i) {

                            ans+=i-tot;
                            tot=i;
                        }
                        tot+=str[i]-'0';
                    }
                }

        fout<<"Case #"<<cases++<<": "<<ans<<endl;
    }

    return 0;

}
