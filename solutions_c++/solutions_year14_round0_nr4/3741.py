#include<iostream>
#include<stdlib.h>
#include<fstream>
using namespace std;
int compara(const void *a, const void *b){
	if ((*(double *)a) > (*(double *)b))
		return 1;
	else
		if ((*(double *)a) < (*(double *)b))
			return -1;
		else
			return 0;
}
int n;
double a[1010],b[1010];
bool mark[1010];
int mayorsinusar(){
    for(int j=n-1;j>=0;j--)
        if(mark[j] == false)
            return j;
    return 0;
}
void usomimenor(){
    for(int j=0;j<n-1;j++)
        if(mark[j] == false)
        {
            mark[j] = true;
            j = n;
        }
}
void usomimayormascercana(double aux){
    for(int j=0;j<n;j++)
        if(b[j] > aux && mark[j] == false)
        {
            mark[j] = true;
            j=n;
        }
}
int main(){
    int t;
    int sol1,sol2;
    ifstream lectura;
    ofstream myfile;
    myfile.open("salida8.txt");
    lectura.open("D-large.in");
    lectura >> t;
  //  cin >> t;
    for(int kase=0;kase<t;kase++){
        lectura >> n;
        //cin >> n;
        for(int i=0;i<n;i++)
        {
            mark[i] = false;
            lectura >> a[i];
            //cin >> a[i];
        }
        for(int i=0;i<n;i++)
            lectura >> b[i];
          //  cin >> b[i];
        qsort(a,n,sizeof(a[0]),compara);
        qsort(b,n,sizeof(b[0]),compara);
        
        int dera=n-1,derb=n-1,izqa=0,izqb=0,mypoints=0;
        for(int i=0;i<n;i++){
            int posm = mayorsinusar();
            if(a[i] < b[posm]){
                usomimayormascercana(a[i]);
            }
            else{
                mypoints++;
                usomimenor();
            }
        }
        
        myfile << "Case #" << kase+1 << ": ";
       //cout << "Case #" << kase+1 << ": ";
        sol2 = mypoints;
        
        dera=n-1;
        derb=n-1;
        izqa=0;
        izqb=0;
        mypoints=0;
        while(izqa <= dera && izqb <= derb){
            if(a[izqa] > b[izqb]){
                izqa++;
                izqb++;
                mypoints++;
            }
            else {
                izqa++;
                derb--;
            }
        }
        
        sol1 = mypoints;
        myfile << sol1 << " " << sol2 << endl;
        //cout << sol1 << " " << sol2 << endl;
        
        
    }
    myfile.close();
}