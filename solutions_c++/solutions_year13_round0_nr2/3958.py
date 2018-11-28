#include<iostream>
#include<vector>

using namespace std;

int fmin(vector< vector<int> > a,int n,int m,int &minh,int &minc,int &minr)
{
    int i,j;

    minh = 101;
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            if(minh > a[i][j])
            {
                minh = a[i][j];
                minr = i;
                minc = j;
            }
        }
    }
}

int main()
{
    int T,tt,m,n,i,j,minh,minc,minr,tmp,c_inrow,c_incol;
    vector< vector<int> > a;
    bool iscol,isrow;
    cin >> T;

    for(tt=1;tt<=T;tt++)
    {
        cin >> n >> m;
        //cout << "N : " << n << "M : " << m << endl ;
        for(i=0;i<n;i++)
        {
            vector<int> tmp_vec;

            for(j=0;j<m;j++)
            {
                cin >> tmp;
                tmp_vec.push_back(tmp);
            }
            a.push_back(tmp_vec);
        }
        cout << "Case #" << tt << ": ";

        iscol = isrow = true;
        while(n>1 && m>1)
        {
            iscol = isrow = true;
            //find min
            fmin(a,n,m,minh,minc,minr);
            //cout << "+" << minh << "+" << minr << "+" << minc << "+";
            //check in row
            for(i=0,c_inrow=0;i<m;i++)
            {
                if(a[minr][i] == minh)
                    c_inrow++;
            }
            if(c_inrow < m)
                isrow = false;
            //check in col
            for(i=0,c_incol=0;i<n;i++)
            {
                if(a[i][minc] == minh)
                    c_incol++;
            }
            if(c_incol < n)
                iscol = false;
            //cout << "r" << c_inrow << "c" << c_incol << "ir" << isrow << "ic" << iscol << endl;
            if(!isrow && !iscol)
                break;
            if(iscol)
            {
                for(i=0;i<n;i++)
                    a[i].erase(a[i].begin() + minc);
                //m--;
                m = a[minr].size();
                continue;
            }
            if(isrow)
            {
                a.erase(a.begin() + minr);
                //n--;
                n = a.size();
                continue;
            }



        }
        if(!isrow && !iscol)
            cout << "NO" << endl;
        else
            cout << "YES" << endl;


        a.clear();


    }
    return 0;
}
