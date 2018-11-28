//Getting the digits
#include<iostream.h>
#include<fstream.h>
#include<conio.h>
#include<string.h>

int main()
{
	ifstream in;
        ofstream out;
        in.open("ais.txt");
        out.open("aos.txt");
 	clrscr();

        int cases;
        in>>cases;

        char c;
        int i;
        char input[200];
        for(i=1;i<=cases;i++)
        {
        	in>>input;


                int j,k;

                int array[10];
                for(j=0;j<10;j++)
                	array[j]=0;
                j=0;
                while(j<strlen(input))
                {
                	if(input[j]=='Z')
                        {
                        	input[j]='a';
                                k=0;
                                while(k<strlen(input))
                                {
                                	if(input[k]=='E')
                                        {
                                        	input[k]='a';break;
                                        }
                                        k++;
                                }
                                 k=0;
                                while(k<strlen(input))
                                {
                                	if(input[k]=='R')
                                        {
                                        	input[k]='a';break;
                                        }
                                        k++;
                                }
                                 k=0;
                                while(k<strlen(input))
                                {
                                	if(input[k]=='O')
                                        {
                                        	input[k]='a';break;
                                        }
                                        k++;
                                }
                                array[0]++;

                        }


                        	if(input[j]=='G')
                        {
                        	input[j]='a';
                                k=0;
                                while(k<strlen(input))
                                {
                                	if(input[k]=='E')
                                        {
                                        	input[k]='a';break;
                                        }
                                        k++;
                                }
                                 k=0;
                                while(k<strlen(input))
                                {
                                	if(input[k]=='I')
                                        {
                                        	input[k]='a';break;
                                        }
                                        k++;
                                }
                                 k=0;
                                while(k<strlen(input))
                                {
                                	if(input[k]=='H')
                                        {
                                        	input[k]='a';break;
                                        }
                                        k++;
                                }
                                k=0;
                                 while(k<strlen(input))
                                {
                                	if(input[k]=='T')
                                        {
                                        	input[k]='a';break;
                                        }
                                        k++;
                                }
                                array[8]++;

                        }


                              	if(input[j]=='X')
                        {
                        	input[j]='a';
                                k=0;
                                while(k<strlen(input))
                                {
                                	if(input[k]=='S')
                                        {
                                        	input[k]='a';break;
                                        }
                                        k++;
                                }
                                 k=0;
                                while(k<strlen(input))
                                {
                                	if(input[k]=='I')
                                        {
                                        	input[k]='a';break;
                                        }
                                        k++;
                                }
                                 k=0;
                                array[6]++;

                        }


                              	if(input[j]=='W')
                        {
                        	input[j]='a';
                                k=0;
                                while(k<strlen(input))
                                {
                                	if(input[k]=='T')
                                        {
                                        	input[k]='a';break;
                                        }
                                        k++;
                                }
                                 k=0;
                                while(k<strlen(input))
                                {
                                	if(input[k]=='O')
                                        {
                                        	input[k]='a';break;
                                        }
                                        k++;
                                }
                                 k=0;


                                array[2]++;

                        }
                              	if(input[j]=='U')
                        {
                        	input[j]='a';
                                k=0;
                                while(k<strlen(input))
                                {
                                	if(input[k]=='F')
                                        {
                                        	input[k]='a';break;
                                        }
                                        k++;
                                }
                                 k=0;
                                while(k<strlen(input))
                                {
                                	if(input[k]=='O')
                                        {
                                        	input[k]='a';break;
                                        }
                                        k++;
                                }
                                 k=0;
                                while(k<strlen(input))
                                {
                                	if(input[k]=='R')
                                        {
                                        	input[k]='a';break;
                                        }
                                        k++;
                                }

                                array[4]++;
                        }
                        j++;
                }
                j=0;

                   while(j<strlen(input))
                {
                	if(input[j]=='F')
                        {
                        	input[j]='a';
                                k=0;
                                while(k<strlen(input))
                                {
                                	if(input[k]=='I')
                                        {
                                        	input[k]='a';break;
                                        }
                                        k++;
                                }
                                 k=0;
                                while(k<strlen(input))
                                {
                                	if(input[k]=='V')
                                        {
                                        	input[k]='a';break;
                                        }
                                        k++;
                                }
                                 k=0;
                                while(k<strlen(input))
                                {
                                	if(input[k]=='E')
                                        {
                                        	input[k]='a';break;
                                        }
                                        k++;
                                }

                                array[5]++;
                        }

                        	if(input[j]=='S')
                        {
                        	input[j]='a';
                                k=0;
                                while(k<strlen(input))
                                {
                                	if(input[k]=='E')
                                        {
                                        	input[k]='a';break;
                                        }
                                        k++;
                                }
                                 k=0;
                                while(k<strlen(input))
                                {
                                	if(input[k]=='V')
                                        {
                                        	input[k]='a';break;
                                        }
                                        k++;
                                }
                                 k=0;
                                while(k<strlen(input))
                                {
                                	if(input[k]=='E')
                                        {
                                        	input[k]='a';break;
                                        }
                                        k++;
                                }
                                k=0;
                                 while(k<strlen(input))
                                {
                                	if(input[k]=='N')
                                        {
                                        	input[k]='a';break;
                                        }
                                        k++;
                                }
                                array[7]++;
                        }


                              	if(input[j]=='T')
                        {
                        	input[j]='a';
                                k=0;
                                while(k<strlen(input))
                                {
                                	if(input[k]=='H')
                                        {
                                        	input[k]='a';break;
                                        }
                                        k++;
                                }
                                 k=0;
                                while(k<strlen(input))
                                {
                                	if(input[k]=='R')
                                        {
                                        	input[k]='a';break;
                                        }
                                        k++;
                                }
                                k=0;
                                 while(k<strlen(input))
                                {
                                	if(input[k]=='E')
                                        {
                                        	input[k]='a';break;
                                        }
                                        k++;
                                }
                                 k=0;
                                while(k<strlen(input))
                                {
                                	if(input[k]=='E')
                                        {
                                        	input[k]='a';break;
                                        }
                                        k++;
                                }
                                 k=0;

                                array[3]++;
                        }


                              	if(input[j]=='O')
                        {
                        	input[j]='a';
                                k=0;
                                while(k<strlen(input))
                                {
                                	if(input[k]=='N')
                                        {
                                        	input[k]='a';break;
                                        }
                                        k++;
                                }
                                 k=0;
                                while(k<strlen(input))
                                {
                                	if(input[k]=='E')
                                        {
                                        	input[k]='a';break;
                                        }
                                        k++;
                                }
                                 k=0;


                                array[1]++;
                        }
                        j++;

                }
                j=0;
                while(j<strlen(input))
                {
                	if(input[j]=='I')
                        	array[9]++;
                        j++;
                }


                out<<"Case #"<<i<<": ";
                int l=0,m=0;
           	for(l=0;l<10;l++)
                {
                	while(m<array[l])
                        {
        			out<<l;
                                m++;
                        }
                	m=0;
                }
                out<<endl;


        }



	getch();
        return 0;
}