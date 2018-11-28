#include <stdio.h>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <string.h>

using namespace std;

int main()
{
    int T;
    int X,R,C;
    //scanf("%d",&T);
    int cas=1;
    bool flag=false;
        ifstream fin("D-small-attempt6.in",ifstream::in);
        if(!fin)
          return EXIT_FAILURE;
        ofstream fout("out.out",ofstream::out);
        //scanf("%d",&S);
        //while(fin.peek() != EOF)
        //{
        fin>>T;
        while(T--)
        {

            flag=false;
            fin>>X>>R>>C;
            int min=(R<C)?R:C;
            int a;
            if(X%2==0)
            {
                a=X/2;
            }
            else{a=X/2+1;}
            if(((R*C)%X==0)&&(a<=R)&&(a<=C))
            {
                if(!(X>=4&&a>=min))
                flag=true;
            }



        fout<<"Case #"<<cas++<<": "<<(flag?"GABRIEL":"RICHARD")<<endl;
        //cout<<"Case #"<<cas<<": "<<(flag?"GABRIEL":"RICHARD")<<endl;
        }
        //}
    return 0;
}
