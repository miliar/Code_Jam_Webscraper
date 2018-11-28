#include<fstream>
using namespace std;
int main(){
        ifstream infile("input.txt");
        ofstream outfile("output.txt");
        int len;
	int num=0;
	char* str=new char[200];
	infile>>len;
        while(num!=len){
            infile>>str;
            bool lastplus=str[0]=='+';
            int out=lastplus?0:1;
            for(int i=1;str[i]!='\0';i++){
                if(lastplus && str[i]=='-'){
                    out+=2;
                }
                lastplus=str[i]=='+';
            }
            outfile<<"Case #"<<num+1<<": "<<out<<"\n";
            num++;
        }
        return 0;
}

