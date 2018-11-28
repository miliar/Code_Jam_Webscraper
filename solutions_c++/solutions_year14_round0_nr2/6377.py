#include<bits/stdc++.h>

using namespace std;

int main()
{
    FILE *fp,*fo;
    fp=fopen("input2.txt","r");
    fo=fopen("output2.txt","w");
    int t,y;
    fscanf(fp,"%d",&t);
    for(y=1;y<=t;y++){

        double c,f,x,ans,rate=2.0,spent=0,init=0,temp,prev=1e9;
        fscanf(fp,"%lf %lf %lf",&c,&f,&x);

       // vector<double> v;

        if(x<=rate)
            fprintf(fo,"Case #%d: %.7lf\n",y,x/rate);

        else{
        while(1)
        {
           temp=init+(x/rate);
           if(prev>temp)
            prev=temp;
           else
            break;
          // v.push_back(temp);

           init+=c/rate;
           rate+=f;

        }

         //temp=init+(x/rate);
         //  v.push_back(temp);
       // sort(v.begin(),v.end());

        fprintf(fo,"Case #%d: %.7lf\n",y,prev);

        }
 }

    fclose(fp);
    fclose(fo);
    return 0;
}
