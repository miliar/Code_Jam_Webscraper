#include <iostream>
#include <fstream>
#include <cstdio>

using namespace std;


int main ()
{
    ofstream output("outputfile.txt");
    ifstream input("D-small-attempt4.in");
    int T,i,X,R,C;
    input>>T;
    for(i=1;i<=T;i++){

        input>>X>>R>>C;
        if(X==4){
            if((R==1 && C==1)||(R==2 && C==2)||(R==2 && C==4)||(R==4 && C==2)||(R==4 && C==1)||(R==1 && C==4)||(R==3 && C==3)||(R==3 && C==2)||(R==2 && C==3)||(R==3 && C==1)||(R==1 && C==3)||(R==2 && C==2)||(R==2 && C==1)||(R==1 && C==2))
            {
                output<<"Case #"<<i<<": RICHARD"<<endl;

            }
            else
            {
                output<<"Case #"<<i<<": GABRIEL"<<endl;

            }
        }
        else if(X==3) {
            if((R==1 && C==1)||(R==2 && C==2)|| (R==2 && C==4)||(R==4 && C==2)||(R==4 && C==1)||(R==1 && C==4)||(R==4 && C==4)||(R==3 && C==1)||(R==1 && C==3)||(R==2 && C==1)||(R==1 && C==2))
                {
                    output<<"Case #"<<i<<": RICHARD"<<endl;

            }
            else
            {
                    output<<"Case #"<<i<<": GABRIEL"<<endl;

            }
                }

        else if(X==2) {
            if((R==1 && C==1)||(R==3 && C==1)||(R==1 && C==3)||(R==3 && C==3))

                {
                    output<<"Case #"<<i<<": RICHARD"<<endl;

                }
            else
            {
                               output<<"Case #"<<i<<": GABRIEL"<<endl;

            }
        }
        else if(X==1) {

                                output<<"Case #"<<i<<": GABRIEL"<<endl;

        }
    }

    return 0;
}

