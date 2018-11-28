#include <fstream>
using namespace std;
ifstream f("input.txt");
ofstream g("output.txt");
int main()
{int t;
f>>t;
for(int i=1;i<=t;i++)
 {
     int x,r,c;
     f>>x>>r>>c;
     if (x==1)
        g<<"Case #"<<i<<": Gabriel\n";
     else
     if(x==2)
        {if((r*c)%2==0)
            g<<"Case #"<<i<<": Gabriel\n";
        else
            g<<"Case #"<<i<<": Richard\n";
        }
    else
        if(x==3)
            {if(r==1||c==1)
                g<<"Case #"<<i<<": Richard\n";
            else
                if(r==2&&c==2)
                    g<<"Case #"<<i<<": Richard\n";
                else
                    if((r==2&&c==3)||(r==3&&c==2))
                        g<<"Case #"<<i<<": Gabriel\n";
                    else
                        if((r==2&&c==4)||(r==4&&c==2))
                            g<<"Case #"<<i<<": Richard\n";
                        else
                            if((r==3&&c==4)||(c==3&&r==4))
                                g<<"Case #"<<i<<": Gabriel\n";
                        else
                            if(r==c&&r==4)
                                g<<"Case #"<<i<<": Richard\n";
                                else
                                    if(r==c&&r==3)
                                        g<<"Case #"<<i<<": Gabriel\n";
            }
        else
            if(x==4)
                {if(r==1||c==1)
                    g<<"Case #"<<i<<": Richard\n";
                else
                    if(r==2&&c==2)
                        g<<"Case #"<<i<<": Richard\n";
                    else
                        if((r==2&&c==3)||(r==3&&c==2))
                            g<<"Case #"<<i<<": Richard\n";
                        else
                            if((r==2&&c==4)||(r==4&&c==2))
                                g<<"Case #"<<i<<": Richard\n";
                            else
                                if((r==3&&c==4)||(c==3&&r==4))
                                    g<<"Case #"<<i<<": Gabriel\n";
                                else
                                    if(r==c&&r==4)
                                         g<<"Case #"<<i<<": Gabriel\n";
                                         else
                                            if(r==c&&r==3)
                                                g<<"Case #"<<i<<": Richard\n";
                }

 }
 return 0;
}
