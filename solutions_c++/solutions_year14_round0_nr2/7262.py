#include <iostream>
#include <stdio.h>
FILE *in = fopen("/users/sungpi/documents/B-large.in", "r");
FILE *out = fopen("/users/sungpi/documents/output.txt", "w");
void tc()
{
    static int n = 1;
    double farmcost, toadd, goal;
    fscanf(in, "%lf %lf %lf", &farmcost, &toadd, &goal);
    
    double increase = 2.0;
    double totalfarmcost = 0.0;
    double costmin = goal / increase;
    double costnow = 0.0;
    while(1)
    {
        costnow = goal / increase + totalfarmcost;
        if( costnow <= costmin){
            costmin = costnow;
        }
        else{
            break;
        }
        
        totalfarmcost = totalfarmcost + farmcost / increase;
        increase = increase + toadd;
    }
    fprintf(out, "Case #%d: %.7lf\n", n++, costmin);
}
int main(void)
{
    int t;
    fscanf(in, "%d", &t);
    
    while(t--) tc();
}