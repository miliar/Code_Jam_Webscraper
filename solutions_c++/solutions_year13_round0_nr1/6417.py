#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream in;
    ofstream ou;
    bool ow,xw;
    int testcase,n,o,x,dot,i,j,k,res1;
    char line[5][5];

    in.open("A-large.in", ifstream::in);

    if(in.is_open())
    {
        ou.open("result2.out");
        if(ou.is_open())
        {
            in>>testcase;
            cout<<testcase<<endl;
            for(i=0;i<testcase;i++)
            {
                for(j=0;j<4;j++)
                    in>>line[j];
                for(j=0;j<4;j++)
                    cout<<line[j]<<endl;
                dot=0;
                ow=false;
                xw=false;
                for(j=0;j<4;j++)
                {
                    o=0;
                    x=0;
                    for(k=0;k<4;k++)
                    {
                        if(line[j][k]!='.'){
                            o++;
                            x++;
                            if(line[j][k]=='X')
                                o--;
                            else
                            if(line[j][k]=='O')
                                x--;
                        }else
                        dot++;
                    }
                    if(x==4){xw=true;break;}
                    if(o==4){ow=true;break;}
                }
                if(!(xw||ow))
                for(j=0;j<4;j++)
                {
                    o=0;
                    x=0;
                    for(k=0;k<4;k++)
                    {
                        if(line[k][j]!='.'){
                            o++;
                            x++;
                            if(line[k][j]=='X')
                                o--;
                            else
                            if(line[k][j]=='O')
                                x--;
                        }
                    }
                    if(x==4){xw=true;break;}
                    if(o==4){ow=true;break;}
                }
                if(!(xw||ow)){
                    o=0;
                    x=0;
                    for(j=0;j<4;j++)
                    {
                        if(line[j][j]!='.'){
                            o++;
                            x++;
                            if(line[j][j]=='X')
                                o--;
                            else
                            if(line[j][j]=='O')
                                x--;
                        }
                    }
                    if(x==4){xw=true;}
                    if(o==4){ow=true;}
                }
                if(!(xw||ow)){

                        o=0;
                        x=0;
                    for(j=0;j<4;j++)
                    {
                        if(line[j][4-j-1]!='.'){
                            o++;
                            x++;
                            if(line[j][4-j-1]=='X')
                                o--;
                            else
                            if(line[j][4-j-1]=='O')
                                x--;
                        }
                    }
                    if(x==4){xw=true;}
                    if(o==4){ow=true;}
                }
                if(xw)ou<<"Case #"<<i+1<<": "<<"X won"<<endl;
                else
                if(ow)ou<<"Case #"<<i+1<<": "<<"O won"<<endl;
                else
                if((!(xw||ow))&&dot==0)ou<<"Case #"<<i+1<<": "<<"Draw"<<endl;
                else
                if((!(xw||ow))&&dot>0)ou<<"Case #"<<i+1<<": "<<"Game has not completed"<<endl;
            }
           ou.close();
        }
        in.close();
    }


    return 0;
}
