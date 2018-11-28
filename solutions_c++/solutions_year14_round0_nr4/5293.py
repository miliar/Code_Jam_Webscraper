#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int war (vector<double>, vector<double>, int);
int dwar (vector<double>, vector<double>, int);
int cmp(const void*, const void*);
int victories(vector<double>, vector<double>);

main()
    {int t, c, n, i;
    double naomi[1000], ken[1000];
    vector<double> na, ke;

    cin>>t;

    for(c=1; c<=t; c++)
        {cin>>n;

        for(i=0; i<n; i++)
            {scanf("%lf", &naomi[i]);}
        for(i=0; i<n; i++)
            scanf("%lf", &ken[i]);
        qsort(naomi, n, sizeof(double), cmp);
        qsort(ken, n, sizeof(double), cmp);

        na.clear();
        ke.clear();

        for(i=0; i<n; i++)
            {na.push_back(naomi[i]);
            ke.push_back(ken[i]);}



        cout << "Case #" << c << ": ";
        cout << dwar(na, ke, n);
        cout<< " ";
        cout << war(na, ke, n) << endl;

        }

        return 0;}

int war (vector<double> naomi, vector<double> ken, int n)
    {int i, j, scoren = 0;
    for(i=0; i<n; i++)
        {if(naomi[0] > ken[ken.size()-1])
            {scoren += (n-i);
            break;}
        else for(j=0; (j<ken.size()); j++)
            if(ken[j] > naomi[0])
                {naomi.erase(naomi.begin());
                ken.erase(ken.begin()+j);
                break;}}
    return scoren;}


int dwar (vector<double> naomi, vector<double>ken, int n)
    {int i, j, scorea = 0, scoreb=0, v, dw;
    scorea=victories(naomi, ken);
    while(naomi.size()>1)
        {naomi.erase(naomi.begin());
        ken.erase(ken.begin()+ken.size()-1);
        v = victories(naomi, ken);
        dw = dwar(naomi, ken, n-1);
        if (v>dw)
            scoreb = v;
        else
            scoreb = dw;
        //cout<<"vics: "<< scorea << " e"<<scoreb<<endl;
            if (scorea > scoreb)
                return scorea;
            scorea = scoreb;}

        return scorea;}

int victories(vector<double> naomi, vector<double>ken)
    {int i, v=0;
    for(i=0; i<naomi.size(); i++)
        if(naomi[i] > ken[i])
           v++;
    return v;}



int cmp(const void *x, const void *y)
    {double xx = *(double*)x, yy = *(double*)y;
  if (xx < yy) return -1;
  if (xx > yy) return  1;
  return 0;
}



