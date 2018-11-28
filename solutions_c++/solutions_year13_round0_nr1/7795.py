#include<iostream>
#include<cstring>
#include<cstdio>
#include<fstream>
using namespace std;
int main()
{
    int t,i,k=1,flag,j,rx,ro,cx,co,rt,ct,f;
    string c[5];
    ifstream of;
    ofstream ef;
    of.open("A-large.in");
    ef.open("output.txt");
    of>>t;
    while(t--)
    {
        flag=rx=ro=cx=co=rt=ct=f=0;
        char s,ch,chr;
        int arr[3]={0},arr1[3]={0};
        for(i=0;i<4;i++)
        of>>c[i];

        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(c[i][j]=='X')
                rx++;
                else if(c[i][j]=='O')
                ro++;
                else if(c[i][j]=='T')
                rt++;

                if(c[j][i]=='X')
                cx++;
                else if(c[j][i]=='O')
                co++;
                else if(c[j][i]=='T')
                ct++;

                if(c[i][j]=='.')
                flag=1;
            }

            if((rx==4) || (rx==3 && rt==1))
            {
                ef<<"Case #"<<k++<<": X won\n";
                f=1;
                break;
            }
            else if((ro==4) || (ro==3 && rt==1))
            {
                ef<<"Case #"<<k++<<": O won\n";
                f=1;
                break;
            }
            else if((cx==4) || (cx==3 && ct==1))
            {
                ef<<"Case #"<<k++<<": X won\n";
                f=1;
                break;
            }
            else if((co==4) || (co==3 && ct==1))
            {
                ef<<"Case #"<<k++<<": O won\n";
                f=1;
                break;
            }

            if(c[i][i]=='X')
            arr[0]++;
            else if(c[i][i]=='O')
            arr[1]++;
            else if(c[i][i]=='T')
            arr[2]++;

            if(c[i][3-i]=='X')
            arr1[0]++;
            else if(c[i][3-i]=='O')
            arr1[1]++;
            else if(c[i][3-i]=='T')
            arr1[2]++;

            rx=ro=cx=co=rt=ct=0;
        }
        if(f==1)
        continue;

        if(arr[0]==4 || (arr[0]==3 && arr[2]==1))
        {
            ef<<"Case #"<<k++<<": X won\n";
            continue;
        }
        else if(arr[1]==4 || (arr[1]==3 && arr[2]==1))
        {
            ef<<"Case #"<<k++<<": O won\n";
            continue;
        }
        else if(arr1[0]==4 || (arr1[0]==3 && arr1[2]==1))
        {
            ef<<"Case #"<<k++<<": X won\n";
            continue;
        }
        else if(arr1[1]==4 || (arr1[1]==3 && arr1[2]==1))
        {
            ef<<"Case #"<<k++<<": O won\n";
            continue;
        }

        //printf("Case #%d: %c won\n",k++,ch);
        if(flag==1)
        ef<<"Case #"<<k++<<": Game has not completed\n";
        //printf("Case #%d: Game has not completed\n",k++);
        else
        ef<<"Case #"<<k++<<": Draw\n";
        //printf("Case #%d: Draw\n",k++);
    }
    //of.close();
    ef.close();
    //system("pause");
    return 0;
}
