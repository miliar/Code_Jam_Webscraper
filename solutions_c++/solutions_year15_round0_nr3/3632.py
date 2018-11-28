#include<cstdio>
#include<cstdlib>

const int count[5][5]={{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};
int t,l,x,store[11000],test[44000];


int cal(int a, int b)
{
int tmp=count[abs(a)][abs(b)];
tmp=tmp*a*b/abs(a)/abs(b);
return tmp;
}

void formtest(int start)
{
for(int i=0;i<l;i++)
{
test[i+l]=test[i+l*2]=test[i+l*3]=test[i]=store[start];
start=(start+1)%l;
}
return;
}


int testtest(int res)
{
int tmp;
if(test[0]==res)return 0;
tmp=test[0];
for(int i=0;i<4*l-1;i++)
{
tmp=cal(tmp,test[i+1]);
if(tmp==res)return i+1;
}
return -1;
}





int main()
{
FILE *fin,*fout;
fin=fopen("3.in","r");
fout=fopen("3.out","w");
fscanf(fin,"%d",&t);
int tmp;

for(int ttmp=0;ttmp<t;ttmp++)
{
fscanf(fin,"%d %d",&l,&x);
getc(fin);
char tmp;
for(int i=0;i<l;i++)
{tmp=getc(fin);
if(tmp=='i')store[i]=2;
else if(tmp=='j')store[i]=3;
else store[i]=4;}
getc(fin);

int line=1,col=0;

/*i*/
formtest(0);
tmp=testtest(2);
line+=(col+tmp+1)/l;
col=(col+tmp+1)%l;
if(tmp==-1 || line > x){fprintf(fout,"Case #%d: NO\n",ttmp+1);continue;}


/*j*/
formtest(col);
tmp=testtest(3);
line+=(col+tmp+1)/l;
col=(col+tmp+1)%l;
if(tmp==-1 || line > x){fprintf(fout,"Case #%d: NO\n",ttmp+1);continue;}

/*k*/
formtest(col);
tmp=testtest(4);
line+=(col+tmp+1)/l;
col=(col+tmp+1)%l;
if(tmp!=-1 && line==x+1 && col==0){fprintf(fout,"Case #%d: YES\n",ttmp+1);continue;}
if(tmp==-1 || line > x){fprintf(fout,"Case #%d: NO\n",ttmp+1);continue;}

/*rest*/
formtest(col);
tmp=test[0];
for(int i=0; i<((x-line)%4)*l+l-col-1;i++)
tmp=cal(tmp,test[i+1]);

if(tmp==1)fprintf(fout,"Case #%d: YES\n",ttmp+1);
else fprintf(fout,"Case #%d: NO\n",ttmp+1);

}
fclose(fin);
fclose(fout);
return 0;
}

