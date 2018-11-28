#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int t;
    ofstream out;

    out.open("output.txt",ios::out);

    cin >> t;

    for(int T=0;T<t;T++)
    {
      int r, c, m;

      cin >> r >> c >> m;

      out << "Case #" << T+1 << ": " << endl;

      if(r==c && c==1)
      {
        if(m==1)
            out << "Impossible" << endl;
        else
            out<<'c'<<endl;
      }
        else if(r*c == m+1)
        {
            for(int i=0;i<r;i++)
            {
                for(int j=0;j<c;j++)
                {
                    out<< (m > 0 ? '*': 'c');
                    m--;
                }

                out<<endl;
            }
        }
        else if(r==1 || c==1)
        {
            if(r*c >= m + 2)
            {
                for(int i=0;i<r;i++)
                {
                    for(int j=0;j<c;j++)
                    {
                        out << (m > 0 ? '*': m==-1 ? 'c': '.');
                        m--;
                    }
                    out << endl;
                }
            }else
            {
                out << "Impossible" << endl;
            }
        }
        else if(r * c -m == 7 || r * c -m == 5)
        {
            out << "Impossible" << endl;
        }
        else if((r==2 || c==2)&&(r*c-m)%2==1)
        {
            out << "Impossible" << endl;
        }
        else
        {
            if(r*c >= m + 4)
            {
                int points = r*c - m - 4;
                int p2=0, p3=0;

                for(int i=0;i<r;i++)
                {
                    if(i==0)
                    {
                        if(points % 2 == 1)
                        {
                            p3 = 3;
                        }

                        points -= p3;
                        p2 = points/2;
                        points -= p2;
                    }

                    if(i==1) points += p2;
                    if(i==2) points += p3;

                    for(int j=0;j<c;j++)
                    {
                        if(i+j==0)
                            out<<'c';
                        else if(j<2 && i<2)
                            out<<'.';
                        else if(j==c-1 && points==2 && i!=0)
                            out<<'*';
                        else if(points>0)
                        {
                            out<<'.';
                            points--;
                        }
                        else
                            out<<'*';
                   }

                out<<endl;
                }

        }else
        {
            out << "Impossible" << endl;
        }
      }
    }
}
