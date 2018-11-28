#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int T;
vector<double> n,k;
int N;
int pole[1047];
int ID[1047];
int vysledokt,vysledokl;

int nacitaj_vstup()
	{
	 double r;
	 n.clear();k.clear();
	 for (int o=1;o<=N;o++)
	 	{
	 	 cin>>r;
	 	 n.push_back(r);
	 	}
	 for (int o=1;o<=N;o++)
	 	{
	 	 cin>>r;
	 	 k.push_back(r);
		}
	 sort(n.begin(),n.end());
	 sort(k.begin(),k.end());
	 for (int o=0;o<=1047;o++) {pole[o]=0;ID[o]=-1;}
	 return 0;
	}

int najdi(int akt,int poz)//akt, pre ktory vrchol to robim, a poz je tip, kde by to mohlo byt
	{
	 while((k[poz]>n[akt])&&(poz>=0))
	 	{
	 	 poz--;
	 	}
	 //teraz je na pozicii mensia hodnota ako na akt
	 if (poz!=-1) {pole[akt-poz]++;ID[akt]=akt-poz;}
	 if (akt>=0) {najdi(akt-1,min(poz,akt-1));}
	 else {return 0;}
	 return 0;
	}

int kont()
	{
	 cout<<"IDs:"<<endl;
	 for (int i=0;i<N;i++) {cout<<ID[i]<<" ";}
	 cout<<endl;
	 cout<<"Pole:"<<endl;
	 for (int i=0;i<N;i++) {cout<<pole[i]<<" ";}
	 cout<<endl<<endl;
	}

int funky(int xn,int xk)
	{
	 while ((k[xk]<n[xn])&&(xk<=N-1))
	 	{
	 	 xk++;
	 	}
	 if (xk>N-1) {return xn;}
	 else {return funky(xn+1,xk+1);}
	}

int put_output(int a,int b,int c)
	{
	 printf("%s","Case #");
	 printf("%d",a);
	 printf("%s",": ");
	 printf("%d",b);
	 printf("%s"," ");
	 printf("%d",c);
	 printf("\n");
	}

int main()
{
	int sucet;
    cin>>T;
    for (int u=1;u<=T;u++)
    	{
    	 vysledokt=0;
    	 vysledokl=0;
		 sucet=0;
		 cin>>N;
    	 nacitaj_vstup();
    	 najdi(N-1,N-1);
    	 
		 //kont();
    	 //ok, now we have precoputed some info, now try to sacristife some first j numbers
    	 for (int j=0;j<=N;j++)
    	 	 {
    	 	  sucet+=pole[j];
    	 	  //cout<<"obetuvavam "<<j<<" cisel"<<endl;
    	 	  //cout<<"teraz som pripocital:"<<pole[j]<<endl;
    	 	  if (j!=0)
    	 	  	 {
    	 	  	  int a;
    	 	  	  a=ID[j-1];
    	 	  	  //cout<<"aktualne cislo malo ID: "<<ID[j-1]<<endl;
    	 	  	  if ((a>j)&&(a>=0)) {pole[a]--;}
    	 	  	  if ((a<=j)&&(a>=0)) {pole[a]--;sucet--;}
    	 	  	 }
    	 	  //cout<<"aktualny sucet:"<<sucet<<endl;
    	 	  vysledokt=max(vysledokt,sucet);
			 }
		 //kont();
		 //cout<<vysledokt<<endl;
		 //now we're gonna compute the result for "easier" version of that wars
		 vysledokl=N-funky(0,0);//return the number, when ken has no number, to defeat Naomi
		 //cout<<vysledokl<<endl;
		 put_output(u,vysledokt,vysledokl);
    	}
	return 0;
}
