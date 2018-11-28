#include<fstream>
#include<iostream>
#include<string>
using namespace std;
char s[101];
int i=1;
bool checkString(string st);
int main(){
    ofstream outFile("output.in");
    ifstream inFile("B-large.in");
    inFile.getline(s, 101);
    int T=stoi(s);
    while(!inFile.eof()){
        string st;
        inFile.getline(s,101);
        st=s;
        int cnt=0;
        while(!checkString(st)){
            if(st.size()==1){
                if(st=="+") continue;
                else{
                    cnt++;
                    st="+";
                }
            }
            else{
                for(int i=0;i<st.size()-1;i++){
                    if(st[i]=='+'&&st[i+1]=='+') continue;
                    else if(st[i]=='-'&&st[i+1]=='-'){
                        if(i!=st.size()-2) continue;
                        else{
                            for(int j=0;j<st.size();j++)
                                st[j]='+';
                            cnt++;
                        }
                    }
                    else if(st[i]=='-'&&st[i+1]=='+'){
                        for(int j=0;j<=i;j++)
                            st[j]='+';
                        cnt++;
                    }
                    else if(st[i]=='+'&&st[i+1]=='-'){
                        int j=i+1;
                        while(st[j]=='-'&&j<st.size()){
                            j++;
                        }
                        for(int k=i+1;k<j;k++)
                            st[k]='+';
                        cnt+=2;
                        i=j-1;
                    }
                }
            }
        }
        if(i==101)break;
        outFile<<"Case #"<<i<<": "<<cnt<<endl;
        i++;
    }
    inFile.close();
    outFile.close();
}

bool checkString(string st){
    for(int i=0;i<st.size();i++){
        if(st[i]=='-') return false;
    }
    return true;
}
