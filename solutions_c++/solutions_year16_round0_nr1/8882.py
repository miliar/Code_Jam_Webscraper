#include<iostream>
#include<fstream>
#include<conio.h>

using namespace std;

int main()
{
	ifstream f;
	f.open("./A-large.in");
	if(f != NULL)
	{
        int tc;
        long num,temp;
        ofstream f2;
        f2.open("./output.txt",ios::out);
        f>>tc;
        for(int i=1;i<=tc;i++){
            f>>num;
                int digit[10]={-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
                int d,j,m=1;
                temp = num;
                do{
                        if(temp == 0){
                            f2<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
                            break;
                        }
                        again:
                        while(temp != 0){
                            d = temp % 10;
                            temp /= 10;
                            for(j=0;j<10;){
                                if(digit[j]== -1){
                                        digit[j] = d;
                                        break;
                                }
                                else
                                    if(digit[j]== d){
                                        break;
                                    }
                                else{
                                        j++;
                                }
                            }
                        }
                        if(digit[9] == -1)
                        {
                            m++;
                            temp = num*m;
                            goto again;
                        }
                        if(digit[9]!= -1){
                            f2<<"Case #"<<i<<": "<<num*m<<endl;
                            break;
                        }
                }while(digit[9] != -1);
            }
            f.close();
            f2.close();
    }
	return 0;
}

