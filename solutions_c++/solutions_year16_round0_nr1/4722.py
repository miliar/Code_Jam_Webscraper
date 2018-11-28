#include<iostream>
#include<fstream>
using namespace std;

main (){
    ifstream inn;
    inn.open("A-large.in");
    ofstream out;
    out.open("out.txt");
    long long casenum;
    inn>>casenum;
    long long num=0;
    bool d0 = false;
    bool d1 = false;
    bool d2 = false;
    bool d3 = false;
    bool d4 = false;
    bool d5 = false;
    bool d6 = false;
    bool d7 = false;
    bool d8 = false;
    bool d9 = false;

    for(long long i=1;i<=casenum;i++)
    {
        d0=d1=d2=d3=d4=d5=d6=d7=d8=d9 = false ;

    	inn>>num;
    	int j=1;
    	if (num==0)
        {
            out<<"Case #"<<i<<": INSOMNIA"<<endl;
            continue;
        }
    	while (1)
        {
            long long x = j*num;
            int y = 0;
            while (x!=0)
            {
                y = x%10;
                    switch(y){
                case 0 :
                    d0=true;
                    break;
                case 1:
                    d1=true;
                    break;
                case 2 :
                    d2=true;
                    break;
                case 3:
                    d3=true;
                    break;
                case 4:
                    d4=true;
                    break;
                case 5:
                    d5=true;
                    break;
                case 6:
                    d6=true;
                    break;
                case 7:
                    d7=true;
                    break;
                case 8:
                    d8=true;
                    break;
                case 9 :
                    d9=true;
                    break;
                    }
                    x=x/10;
            }
            if (d0==true and d1==true and d2==true and d3==true and d4==true and d5==true and d6==true and d7==true and d8==true and d9==true)
            {
                out<<"Case #"<<i<<": "<<j*num<<endl;
                break;
            }
            j++;
        }

	}
}
