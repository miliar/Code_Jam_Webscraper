#include<iostream.h>
#include<fstream.h>
#include<conio.h>
void main()
{
		 char t[4][4];        clrscr();
		 int i=0,j=0,k=0,x=0,y=0,d=0,test=0,T;
		 ifstream r;
		 ofstream w;
		 r.open("A.in",ios::in);
		 w.open("Jam1a.txt",ios::out);
		 r>>T;

		 while(test++<T)
		 {
				 i=0;j=0;k=0;x=0;y=0;d=0;
				 for(k=0;k<16;)
				 {
					 r>>t[i][j];
					 if((t[i][j]=='X')||(t[i][j]=='O')||(t[i][j]=='T')||(t[i][j]=='.'))
						 {j++;k++;}
					 if(j==4)
					 {
								 i++;
								 j=0;
					 }
				 }

				 j=0;
				 for(i=0;i<4;i++,x=0,y=0)
					 for(j=0;j<4;j++)
					 {
						 switch(t[i][j])
						 {
							case 'X': x++; break;
							case 'O': y++; break;
							case 'T': x++; y++; break;
							case '.': d++; break;
							default : break;
						 }

						if(x==4||y==4)
						 { goto end; }
					 }

				 for(i=0,x=0,y=0;i<4;i++,x=0,y=0)
					 for(j=0;j<4;j++)
					 {
						 switch(t[j][i])
						 {
							case 'X': x++; break;
							case 'O': y++; break;
							case 'T': x++; y++; break;
							default : break;
						 }
						 if(x==4||y==4)
						 { goto end; }
						}

						for(i=0,j=0;j<4;j++,i++)
						{
						 switch(t[j][i])
						 {
							case 'X': x++; break;
							case 'O': y++; break;
							case 'T': x++; y++; break;
							default : break;
						 }

						 if(x==4||y==4)
						 { goto end; }
						}

						for(i=0,j=3,x=0,y=0;i<4;j--,i++)
						{
						 switch(t[i][j])
						 {
							case 'X': x++; break;
							case 'O': y++; break;
							case 'T': x++; y++; break;
							default : break;
						 }

						 if(x==4||y==4)
						 { goto end; }
						}

		 end:
				 if(x==4)
							w<<"Case #"<<test<<": X won\n";
				 else if(y==4)
							w<<"Case #"<<test<<": O won\n";
				 else if(d==0)
							w<<"Case #"<<test<<": Draw\n";
				 else
							w<<"Case #"<<test<<": Game has not completed\n";
		 }
		 getch();
		r.close();
		w.close();
}