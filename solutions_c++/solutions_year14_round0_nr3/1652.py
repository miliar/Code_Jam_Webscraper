#include<fstream.h>
#include<math.h>
#include<iostream.h>
#include<conio.h>

char array[230];

char pos[50][50];

char result(void);

int c,r,m,n;

void main()
 {
  clrscr();
  int i,j,k,cases,a,l,sqr;
  char junk;
  ifstream filin;
  filin.open("goog3i.in",ios::in);
  ofstream filout;
  filout.open("goog3o.in",ios::out);
  filin>>cases;
  filin.get(junk);
  for (i=0;i<cases;i++)
   {
    filin>>r;
    filin.get(junk);
    filin>>c;
    filin.get(junk);
    filin>>m;
    filin.get(junk);
    n=(r*c)-m;
    sqr=(int)floor(sqrt(n));
    array[i]=result();
    if (c==2&&r>=3&&n==2)
      filout<<"Case #"<<i+1<<":"<<'\n'<<"Impossible"<<'\n';
    else
    {
    if (array[i]=='N')
      filout<<"Case #"<<i+1<<":"<<'\n'<<"Impossible"<<'\n';
    else
     {
      if (r==1&&c==1)
	filout<<"Case #"<<i+1<<":"<<'\n'<<"c"<<'\n';
      if (r==2&&c==1&&n==2)
	filout<<"Case #"<<i+1<<":"<<'\n'<<"c"<<'\n'<<"."<<'\n';
      if (r==2&&c==1&&n==1)
	filout<<"Case #"<<i+1<<":"<<'\n'<<"c"<<'\n'<<"*"<<'\n';
      if (r==1&&c==2&&n==2)
	filout<<"Case #"<<i+1<<":"<<'\n'<<"c."<<'\n';
      if (r==1&&c==2&&n==1)
	filout<<"Case #"<<i+1<<":"<<'\n'<<"c*"<<'\n';
      if (r==2&&c==2&&n==1)
	filout<<"Case #"<<i+1<<":"<<'\n'<<"c*"<<'\n'<<"**"<<'\n';
      if (r==2&&c==2&&n==4)
	filout<<"Case #"<<i+1<<":"<<'\n'<<"c."<<'\n'<<".."<<'\n';
      if (c>=3&&r==1)
       {
	filout<<"Case #"<<i+1<<":"<<'\n'<<"c";
	for (j=0;j<n-1;j++)
	  filout<<".";
	for (j=0;j<m;j++)
	  filout<<"*";
	filout<<'\n';
       }
      if (r>=3&&c==1)
       {
	filout<<"Case #"<<i+1<<":"<<'\n'<<"c"<<'\n';
	for (j=0;j<n-1;j++)
	  filout<<"."<<'\n';
	for (j=0;j<m;j++)
	  filout<<"*"<<'\n';
       }
      if (r==2&&c>=3&&n==1)
       {
       filout<<"Case #"<<i+1<<":"<<'\n'<<"c";
       for (j=0;j<m/2;j++)
	 filout<<"*";
       filout<<'\n';
       for(j=0;j<(m+2)/2;j++)
	 filout<<"*";
       filout<<'\n';

       }
      else
      if (c>=3&&r==2)
       {
	filout<<"Case #"<<i+1<<":"<<'\n'<<"c";
	for (j=0;j<(n-2)/2;j++)
	  filout<<".";
	for (j=0;j<m/2;j++)
	  filout<<"*";
	filout<<'\n';
	for (j=0;j<n/2;j++)
	  filout<<".";
	for (j=0;j<m/2;j++)
	  filout<<"*";
	filout<<'\n';
       }
      if (r>=3&&c==2&&n==1)
       {
       filout<<"Case #"<<i+1<<":"<<'\n'<<"c*"<<'\n';
       for(j=0;j<m/2;j++)
	filout<<"**"<<'\n';
       }
      else
      if (r>=3&&c==2)
       {
	filout<<"Case #"<<i+1<<":"<<'\n'<<"c."<<'\n';
	for (j=0;j<(n-2)/2;j++)
	  filout<<".."<<'\n';
	for (j=0;j<m/2;j++)
	  filout<<"**"<<'\n';
       }
      if (r>=3&&c>=3)
       {
	if (sqr<r&&sqr<c)
	 {
	  for (j=0;j<r;j++)
	    for (k=0;k<c;k++)
	      pos[j][k]='*';
	  for (j=0;j<sqr;j++)
	    for (k=0;k<sqr;k++)
	      pos[j][k]='.';
	  pos[0][0]='c';
	  if (n==pow(sqr,2)+1)
	   {
	    pos[sqr-1][sqr-1]='*';
	    pos[sqr][0]='.';
	    pos[sqr][1]='.';
	   }
	  if ((n>pow(sqr,2)+1)&&(n<=(pow(sqr,2)+sqr)))
	   {
	    for (j=0;j<n-pow(sqr,2);j++)
	      pos[sqr][j]='.';
	   }
	  if (n==pow(sqr,2)+sqr+1)
	   {
	    for (j=0;j<(sqr-1);j++)
	      pos[sqr][j]='.';
	    pos[0][sqr]='.';
	    pos[1][sqr]='.';
	   }
	  if (((n-pow(sqr,2)-sqr)>=2)&&((n-pow(sqr,2)-sqr)<=sqr))
	   {
	    for (j=0;j<sqr;j++)
	      pos[sqr][j]='.';
	    for (j=0;j<(n-pow(sqr,2)-sqr);j++)
	      pos[j][sqr]='.';
	   }
	 }
	if (r<=sqr&&r<c)
	 {
	  for (j=0;j<r;j++)
	    for (k=0;k<c;k++)
	      pos[j][k]='*';
	  for (j=0;j<r;j++)
	    for (k=0;k<r;k++)
	      pos[j][k]='.';
	  pos[0][0]='c';
	  for (j=0;j<(int)((n-(int)pow(r,2))/r);j++)
	    for (k=0;k<r;k++)
	      pos[k][r+j]='.';
	  for (l=0;l<(int)((n-(int)pow(r,2))%r);l++)
	    pos[l][r+j]='.';
	  if (l==1)
	   {
	    pos[1][r+j]='.';
	    pos[r-1][r+j-1]='*';
	   }
	 }
	if (c<=sqr&&c<=r)
	 {
	  for (j=0;j<r;j++)
	    for (k=0;k<c;k++)
	      pos[j][k]='*';
	  for (j=0;j<c;j++)
	    for (k=0;k<c;k++)
	      pos[j][k]='.';
	  pos[0][0]='c';
	  for (j=0;j<(int)((n-(int)pow(c,2))/c);j++)
	    for (k=0;k<c;k++)
	      pos[c+j][k]='.';
	  for (l=0;l<(int)((n-(int)pow(c,2))%c);l++)
	    pos[c+j][l]='.';
	  if (l==1)
	   {
	    pos[c+j][1]='.';
	    pos[c+j-1][c-1]='*';
	   }
	 }
	filout<<"Case #"<<i+1<<":"<<'\n';
	for (j=0;j<r;j++)
	 {
	  for (k=0;k<c;k++)
	    filout<<pos[j][k];
	  filout<<'\n';
	 }
       }
     }}
   }
  filin.close();
  filout.close();
 }

char result(void)
 {
  if (c>=3&&r>=3&&(n==2||n==3||n==5||n==7))
    return 'N';
  if (r==2&&c>=3&&(n%2==1)&&n!=1)
    return 'N';
  if (r==2&&c>=3&&n==2)
    return 'N';
  if (c==2&&r>=3&&(n%2==1)&&n!=1)
    return 'N';
  if (c==2&&r>=3&&n==2)
    return 'N';
  if (c==2&&r==2&&(n==2||n==3))
    return 'N';
  return 'Y';
 }