#include<iostream>
#include<stdio.h>
using namespace::std;
int main()
{
    int testcase,i,j,numt=1,xcount=0,ocount=0,tcount=0,flag=0;
    cin>>testcase;char arr[4][4];
    FILE *fp=fopen("file.txt","w");
    while(numt<=testcase)
    {
        flag=0;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                cin>>arr[i][j];
        for(i=0;i<4;i++)
        {
            xcount=0;ocount=0;tcount=0;
            for(j=0;j<4;j++)
            {
                if(arr[i][j]=='X')
                    xcount++;
                else if(arr[i][j]=='O')
                    ocount++;
                else if(arr[i][j]=='T')
                    tcount++;
            }
            if(xcount==4 || (xcount==3 && tcount==1))
            {
            	fprintf(fp,"Case #%d: X won\n",numt);
                cout<<"Case #"<<numt<<": X won\n";flag=1;break;
            }
            if(ocount==4 || (ocount==3 && tcount==1))
            {
            	fprintf(fp,"Case #%d: O won\n",numt);
                cout<<"Case #"<<numt<<": O won\n";flag=1;break;
            }
        }
        if(!flag)
        {
            for(i=0;i<4;i++)
            {
                xcount=0;ocount=0;tcount=0;
                for(j=0;j<4;j++)
                {
                    if(arr[j][i]=='X')
                        xcount++;
                    else if(arr[j][i]=='O')
                        ocount++;
                    else if(arr[j][i]=='T')
                        tcount++;
                }
                if(xcount==4 || (xcount==3 && tcount==1))
                {
            	fprintf(fp,"Case #%d: X won\n",numt);
                    cout<<"Case #"<<numt<<": X won\n";flag=1;break;
                }
                if(ocount==4 || (ocount==3 && tcount==1))
                {
            	fprintf(fp,"Case #%d: O won\n",numt);
                    cout<<"Case #"<<numt<<": O won\n";flag=1;break;
                }
            }
        }
		if(!flag)
        {
        	xcount=0;ocount=0;tcount=0;
            for(i=0;i<4;i++)
            {
                if(arr[i][3-i]=='X')
                	xcount++;
               	else if(arr[i][3-i]=='O')
               		ocount++;
          		else if(arr[i][3-i]=='T')
          			tcount++;
        	}
            if(xcount==4 || (xcount==3 && tcount==1))
            {fprintf(fp,"Case #%d: X won\n",numt);
                cout<<"Case #"<<numt<<": X won\n";flag=1;
            }
            if(ocount==4 || (ocount==3 && tcount==1))
            {
            	fprintf(fp,"Case #%d: O won\n",numt);
                cout<<"Case #"<<numt<<": O won\n";flag=1;
            }
            
        }
        if(!flag)
        {
            xcount=0;ocount=0;tcount=0;
            for(i=0;i<4;i++)
            {
                if(arr[i][i]=='X')
                    xcount++;
                else if(arr[i][i]=='O')
                    ocount++;
                else if(arr[i][i]=='T')
                    tcount++;
            }
            if(xcount==4 || (xcount==3 && tcount==1))
            {
            	
            	fprintf(fp,"Case #%d: X won\n",numt);
                cout<<"Case #"<<numt<<": X won\n";flag=1;
            }
            if(ocount==4 || (ocount==3 && tcount==1))
            {
            	fprintf(fp,"Case #%d: O won\n",numt);
                cout<<"Case #"<<numt<<": O won\n";flag=1;
            }
        }
        if(!flag)
        {
            for(i=0;i<4;i++)
            {
                for(j=0;j<4;j++)
                {
                    if(arr[i][j]=='.')
                    {
            			fprintf(fp,"Case #%d: Game has not completed\n",numt);
                        cout<<"Case #"<<numt<<": Game has not completed\n";flag=1;break;
                    }
                }
                if(flag)
                    break;
            }
        }
        if(!flag)
        {
       	fprintf(fp,"Case #%d: Draw\n",numt);
            cout<<"Case #"<<numt<<": Draw\n";
        }
        numt++;
        cout<<endl;
    }
}
