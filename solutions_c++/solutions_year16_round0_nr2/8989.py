#include<iostream>
#include<fstream>
#include<string.h>

using namespace std;

int solve(char s[],int l){
    char plus = '+';
    char minus = '-';
    int i=1,flip=0;

    if(l == 1){
        if(s[0]==minus){
            s[0]=plus;
            flip++;
        }
    }
    else{
        do{
            char top = s[0];
            i=1;
            while(s[i]==top){
                i++;
            }
                if(top == plus){
                        if(i == l)
                            break;
                    for(int j=0;j<=i;j++){
                        s[j]=minus;
                    }
                    flip++;
                }
                else if(top == minus){
                    for(int j=0;j<=i;j++){
                        s[j]=plus;
                    }
                    flip++;
                }

        }while(i!=l);
        if(s[l-1] == minus){cout<<" last ";
            for(int j=0;j<l;j++){
                s[j]=plus;
                flip++;
            }
        }
    }
    return flip;
}

int main()
{
    ifstream f;
    f.open("./B-large.in",ios::in);
    ofstream f2;
    f2.open("./output.txt",ios::out);
    if(f != NULL)
    {

        int tc;
        f>>tc;  //to get no. of test cases
        f.get();    //to remove extra newline before test case condition begin
        int caseno=1;
        do{
                char str[110];
                char ch;
                int i = 0,l;
                do{
                    ch=f.get();
                    if(ch == '+' || ch == '-'){
                        str[i]=ch;
                        i++;
                    }else
                    if(ch == '\n'){
                        str[i]='\0';
                    }
                    else{
                        str[i]='\0';
                        break;
                    }
                }while(ch != '\n');
                l=strlen(str);
                f2<<"Case #"<<caseno<<": "<<solve(str,l)<<endl;
                caseno++;
        }while(!f.eof());
    }
    f.close();
    f2.close();
	return 0;
}

