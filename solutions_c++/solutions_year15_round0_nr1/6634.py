//by mohit nathrani
#include<iostream.h>
#include<conio.h>
#include<fstream.h>

void main()
{
        clrscr();

        fstream fout;
        fout.open("1.in",ios::out|ios::binary);
        fstream fin;
        fin.open("2.in",ios::in|ios::binary);
        fin.seekg(0);

        int t;
        fin>>t;
        cout<<t;
        long hs,c[10001],m[10001],stand,fri,r=0;
        char tem[15];
        for(int i=0;i<100;i++)
        {
                cout<<endl<<i+1;
                stand=0;
                fri=0;
                r=0;
                fin>>hs;
                cout<<"hs: "<<hs<<endl;
                fin>>tem;
                cout<<"tem :"<<tem<<endl;
                for(int z=0;z<=hs;z++)
                {
                char m=tem[z];
                int n=(int)m;
                cout<<m<<" ";
                c[z]=n-48;
                cout<<c[z]<<endl;
                }

                for(r=0;r<=hs;r++)
                {
                        cout<<c[r];
                }

                for(r=0;r<=hs;r++)
                {
                        if(stand>=r||c[r]==0)
                        {
                         stand+=c[r];
                         cout<<stand;
                        }
                        else
                        {
                         fri+=r-stand;
                         stand+=fri+c[r];
                         cout<<stand;
                        }
                }
                fout<<"Case #"<<i+1<<": "<<fri<<endl;
                }
        fin.close();
        fout.close();
        getch();
}