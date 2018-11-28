#include<iostream>
#include<string>
#include<cstring>
#include<fstream>
using namespace std;
int main(){
    ifstream fin;
    ofstream fout;
    fin.open ("A-large.in");
    fout.open("output_large.out");
    int T;
    fin>>T;
    int counter=0;
    while(counter<T){
        counter++;
        string N;
        fin>>N;
        fout<<"Case #"<<counter<<": ";
        //check for zero
        if(N.length()==1 && N.at(0)=='0'){
            fout<<"INSOMNIA"<<endl;
            continue;
        }
        char * charArray = new char [N.length()+1];
        std::strcpy (charArray, N.c_str());
        bool flag[10]={false};
        int numberArray[20]={0};
        int lengthOfNumber=N.length();
        for(int indexCharArray=lengthOfNumber-1,indexIntArray=0;indexCharArray>-1;indexCharArray--){
            numberArray[indexIntArray++]=(int)(charArray[indexCharArray])-48;
        }
        int multiplier=1;
        bool incomplete=true;
        while(incomplete){
            int newNumber[20]={0};
            int carry=0;
            for(int indexN=0;indexN<lengthOfNumber || carry!=0;indexN++){
                int result=numberArray[indexN]*multiplier+carry;
                newNumber[indexN]=result%10;
                carry=result/10;
                if(!flag[newNumber[indexN]]) flag[newNumber[indexN]]=true;
            }
            //
            /*
            fout<<"#";
            for(int i=0;i<20;i++)
                fout<<newNumber[i];
            fout<<"#"<<endl;
            */
            //
            multiplier++;
            bool allClear=true;
            for(int digit=0;digit<10;digit++)
                allClear&=flag[digit];
            if(allClear) {
                int index=19;
                bool noMoreZeros=false;
                while(index>-1){
                    if(newNumber[index]!=0 || noMoreZeros){
                        fout<<newNumber[index];
                        noMoreZeros=true;
                    }
                    index--;
                }
                fout<<endl;
                incomplete=false;
            }
        }
    }
    fin.close();
    fout.close();
}
