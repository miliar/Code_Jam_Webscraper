#include<iostream>
#include<fstream>
#include<string>
#include<cstring>

using namespace std;

ifstream inFile("C-small-attempt0.in",ios::in);
ofstream oFile("C-small-attempt0.out",ios::out);

int main()
{
    int t, l, n, k;
    string temp, s;
    string c[2];

    c[0] = c[1] = c[2] = " ";
    inFile>>t;

    for(int i=1; i<=t; i++)
    {
        k=0;
        inFile>> l>> n>> s;
        //cout<<s<<" ";

        if(l*n < 3)
        {
            oFile<<"Case #"<<i<<": NO"<<endl;
        }
        else if(l == 1)
        {
            oFile<<"Case #"<<i<<": NO"<<endl;
        }
        else
        {
            temp=s;

            if(n>1)
            {
                for(int j=1; j<n; j++)
                {
                    temp += s;
                }
            }

            c[0] = temp[0];

            for(int j=1; j<l*n; j++)
            {

                    if(k==0 && c[k]=="i")
                    {
                        k=1;
                        c[1] = temp[j];
                        j++;
                    }

                    if(k==1 && c[k]=="j")
                    {
                        k=2;
                        c[2] = temp[j];
                        j++;
                    }

                    if(k==2 && c[k]=="k" && j==n*l)
                    {
                        break;
                    }

                    if(c[k] == "i")
                    {
                        if(temp[j] == 'i')
                            c[k] = "-1";
                        else if(temp[j] == 'j')
                            c[k] = "k";
                        else if(temp[j] == 'k')
                            c[k] = "-j";
                    }
                    else if(c[k] == "-i")
                    {
                        if(temp[j] == 'i')
                            c[k] = "1";
                        else if(temp[j] == 'j')
                            c[k] = "-k";
                        else if(temp[j] == 'k')
                            c[k] = "j";
                    }
                    else if(c[k] == "j")
                    {
                        if(temp[j] == 'i')
                            c[k] = "-k";
                        else if(temp[j] == 'j')
                            c[k] = "-1";
                        else if(temp[j] == 'k')
                            c[k] = "i";
                    }
                    else if(c[k] == "-j")
                    {
                        if(temp[j] == 'i')
                            c[k] = "k";
                        else if(temp[j] == 'j')
                            c[k] = "1";
                        else if(temp[j] == 'k')
                            c[k] = "-i";
                    }
                    else if(c[k] == "k")
                    {
                        if(temp[j] == 'i')
                            c[k] = "j";
                        else if(temp[j] == 'j')
                            c[k] = "-i";
                        else if(temp[j] == 'k')
                            c[k] = "-1";
                    }
                    else if(c[k] == "-k")
                    {
                        if(temp[j] == 'i')
                            c[k] = "-j";
                        else if(temp[j] == 'j')
                            c[k] = "i";
                        else if(temp[j] == 'k')
                            c[k] = "1";
                    }
                    else if(c[k] == "1")
                    {
                        if(temp[j] == 'i')
                            c[k] = "i";
                        else if(temp[j] == 'j')
                            c[k] = "j";
                        else if(temp[j] == 'k')
                            c[k] = "k";
                    }
                    else if(c[k] == "-1")
                    {
                        if(temp[j] == 'i')
                            c[k] = "-i";
                        else if(temp[j] == 'j')
                            c[k] = "-j";
                        else if(temp[j] == 'k')
                            c[k] = "-k";
                    }
                }

                oFile<<"Case #"<<i<< ": ";

                if(c[0] == "i" && c[1] == "j" && c[2] == "k")
                    oFile<< "YES"<<endl;
                else
                    oFile<< "NO"<<endl;
            }
        }

        return 0;
    }
