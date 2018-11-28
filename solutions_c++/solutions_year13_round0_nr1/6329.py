#include<iostream>
#include<string>
using namespace std;
#define SIZE 4
#define MX 0
#define MO 1
#define MFULL 2
#define MB 3

char board[SIZE][SIZE];

void input()
{char ch;
for(int y=0;y<SIZE;y++)
	{string str;cin>>str;
        for(int x=0;x<SIZE;x++)
	board[x][y]=str[x];
}
}

int X,O,T,blank;


void inrvar(char x)
{if(x=='T') T++;
else if(x=='X') X++;
else if(x=='O') O++;
else if(x=='.') blank++;}

void initvar()
{X=O=T=blank=0;}

void rcount(int y)
{for(int x=0;x<SIZE;x++)
inrvar(board[x][y]);}

void ccount(int x)
{for(int y=0;y<SIZE;y++)
inrvar(board[x][y]);}

void d1count()
{for(int x=0,y=0;y<SIZE;x++,y++)
inrvar(board[x][y]);}

void d2count()
{for(int x=SIZE-1,y=0;y<SIZE;x--,y++)
inrvar(board[x][y]);}

int ojudge()
{if(X+T==SIZE) return MX;
else if(O+T==SIZE) return MO;
else if(X+O+T==SIZE) return MFULL;
else return MB;}

void judge()
{bool blankbool;int dec;

for(int a=0;a<SIZE;a++)
{initvar();
rcount(a);
dec=ojudge();
if(dec==MX) {cout<<"X won";return;}
if(dec==MO) {cout<<"O won";return;}
if(dec==MB) {blankbool=true;}}

for(int a=0;a<SIZE;a++)
{initvar();
ccount(a);
dec=ojudge();
if(dec==MX) {cout<<"X won";return;}
if(dec==MO) {cout<<"O won";return;}
if(dec==MB) {blankbool=true;}}

initvar();
d1count();
dec=ojudge();
if(dec==MX) {cout<<"X won";return;}
if(dec==MO) {cout<<"O won";return;}
if(dec==MB) {blankbool=true;}

initvar();
d2count();
dec=ojudge();
if(dec==MX) {cout<<"X won";return;}
if(dec==MO) {cout<<"O won";return;}
if(dec==MB) {blankbool=true;}

if(blankbool==true) cout<<"Game has not completed";
else if(blankbool==false) cout<<"Draw";
return;
}

int main()
{int total;
cin>>total;
for(int mainc=0;mainc<total;mainc++)
{
initvar();
input();
cout<<"Case #"<<mainc+1<<": ";
judge();
cout<<'\n';}}
