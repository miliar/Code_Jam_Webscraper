#include<iostream>
#include<cctype>
using namespace std;
int main()
{
    int n,i;
    cin>>n;
    for(int z=1;z<=n;z++)
    {
          char input[17],buffer;
          input[0]=n;
          int i=1,flagx=0,flago=0,flaginc=0;
          do
            {
                cin>>buffer;
                if(isdigit(buffer)==0 )
                {
                    input[i]=buffer;
                    if(buffer == '.')
                        flaginc=1;
                    i++;
                }

            }while(i<=16);
            for(int j=1;j<=4;j++)
            {
                int xsumh=0,osumh=0;
                for(int k=1;k<=4;k++)
                {
                    if(input[((4*(j-1))+k)] == 'X' || input[((4*(j-1))+k)] == 'T')
                    {
                        xsumh=xsumh+(4*(j-1))+k+1000;
                    }
                    if(input[((4*(j-1))+k)] == 'O' || input[((4*(j-1))+k)] == 'T')
                    {
                        osumh=osumh+(4*(j-1))+k+1000;
                    }
                }
                int xsumv=0,osumv=0;
                for(int k=1;k<=4;k++)
                {
                    if(input[((4*(k-1))+j)] == 'X' || input[((4*(k-1))+j)] == 'T')
                    {
                        xsumv=xsumv+(4*(k-1))+j+1000;
                    }
                    if(input[((4*(k-1))+j)] == 'O' || input[((4*(k-1))+j)] == 'T')
                    {
                        osumv=osumv+(4*(k-1))+j+1000;
                    }
                }
                int xsumc1=0;

                    if(input[1] == 'X' || input[1] =='T')
                    xsumc1=xsumc1+1;
                    if(input[6] == 'X' || input[6] =='T')
                    xsumc1=xsumc1+6;
                    if(input[11] == 'X' || input[11] =='T')
                    xsumc1=xsumc1+11;
                    if(input[16] == 'X' || input[16] =='T')
                    xsumc1=xsumc1+16;

                int xsumc2=0;

                    if(input[4] == 'X' || input[4] =='T')
                        xsumc2=xsumc2+4;
                    if(input[7] == 'X' || input[7] =='T')
                        xsumc2=xsumc2+7;
                    if(input[10] == 'X' || input[10] =='T')
                        xsumc2=xsumc2+10;
                    if(input[13] == 'X' || input[13] =='T')
                        xsumc2=xsumc2+13;

                int osumc1=0;

                    if(input[1] == 'O' || input[1] =='T')
                    osumc1=osumc1+1;
                    if(input[6] == 'O' || input[6] =='T')
                    osumc1=osumc1+6;
                    if(input[11] == 'O' || input[11] =='T')
                    osumc1=osumc1+11;
                    if(input[16] == 'O' || input[16] =='T')
                    osumc1=osumc1+16;

                int osumc2=0;

                    if(input[4] == 'O' || input[4] =='T')
                        osumc2=osumc2+4;
                    if(input[7] == 'O' || input[7] =='T')
                        osumc2=osumc2+7;
                    if(input[10] == 'O' || input[10] =='T')
                        osumc2=osumc2+10;
                    if(input[13] == 'O' || input[13] =='T')
                        osumc2=osumc2+13;

//cout<<" "<<xsumh<<" "<<xsumv<<" "<<osumh<<" "<<osumv<<" "<<xsumc1<<" "<<xsumc2<<" "<<osumc1<<" "<<osumc2<<endl;

                if((xsumh == 4010) || (xsumh == 4026) ||(xsumh == 4042) || (xsumh == 4058) || (xsumv == 4028) || (xsumv == 4032) || (xsumv == 4036) || (xsumv == 4040) || (xsumc1 == 34) || (xsumc2 == 34))
                flagx=1;
                if((osumh == 4010) || (osumh == 4026) ||(osumh == 4042) || (osumh == 4058) || (osumv == 4028) || (osumv == 4032) || (osumv == 4036) || (osumv == 4040) || (osumc1 == 34) || (osumc2 == 34))
                flago=1;
            }
            if(flagx==1)
            {
                cout<<"Case #"<<z<<": X won"<<endl;
                flagx=0;
            }
            else
            if(flago==1)
            {
                cout<<"Case #"<<z<<": O won"<<endl;
                flago=0;
            }
            else
            if(flaginc==1)
            cout<<"Case #"<<z<<": Game has not completed"<<endl;
            else
            cout<<"Case #"<<z<<": Draw"<<endl;

        }
        return 1;
}
