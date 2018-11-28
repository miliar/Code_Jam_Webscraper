#include <stdio.h>

#include <conio.h>

using namespace std;

int main ()
{
    
    FILE *fin;
    fin = fopen("B.txt", "r");
    FILE *fout;
    fout = fopen("B-out.txt", "w");
    
    
    int t;
    double c,f,x;
    
    fscanf (fin, "%d", &t);
    for (int i=1;i<=t;i++){
        fscanf (fin, "%lf %lf %lf", &c,&f,&x);
        
    
    double rate=2.00, time=0.00;
    while (1){
          if (x/rate > (c/rate) + x/(rate+f) ){
             time+=(c/rate);
             rate+=f;
          }
          else {
              time+=x/rate;
              break;
          }
          
    }
        
    fprintf (fout, "Case #%d: %.7lf\n", i,time);    
        
            
    }
    
    
    getch ();
}
