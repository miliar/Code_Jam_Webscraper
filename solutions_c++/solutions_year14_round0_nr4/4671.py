#include<iostream>
#include<fstream>
using namespace std;

typedef float aType;




void cancel(float ar[],int n)
{
    
    for(int i=0;i<n;i++)
    {
            if(ar[i]==0)
            {
                      for(int j=i;j<n;j++)
                      {
                              ar[j]=ar[j+1];
                      }
            }
    }
}








//  prototypes
void Quicksort( aType a[], int first, int last );
int Pivot( aType a[], int first, int last );

void  Swap( aType &v1, aType &v2 );







void Quicksort( aType a[], int first, int last ) 
{
    int pivot;

    if( first < last ) {
        pivot = Pivot( a, first, last );
        Quicksort( a, first, pivot-1 );
        Quicksort( a, pivot+1, last );
    }
}


/*  Pivot:  Find and return the index of pivot element.
 */

int Pivot( aType a[], int first, int last ) 
{
    int  p = first;
    aType pivot = a[first];

    for( int i = first+1 ; i <= last ; i++ ) {
        if( a[i] <= pivot ) {
            p++;
            Swap( a[i], a[p] );
        }
    }

    Swap( a[p], a[first] );

    return p;
}


/*  Swap:  Swap two item (by reference).
 */

void  Swap( aType &v1, aType &v2 )
{
    aType  tmpVal;

    tmpVal = v1;
    v1 = v2;
    v2 = tmpVal;
}





















int main()
{
    ofstream fout ("test.out");
    ifstream fin ("test.in");
    int tes;
    fin>>tes;
    for(int u=1;u<=tes;u++)
    {
       int t;
       fin>>t; 
       float a[t],b[t],c[t],d[t];
       for(int i=0;i<t;i++)
       {
           fin>>c[i];
           a[i]=c[i];
       }
       for(int i=0;i<t;i++)
       {
           fin>>d[i];
           b[i]=d[i];
       }
       
    // a[2]={0.7,0.2};
     //b[2]={0.8,0.3};
    int p1=0,p2=0;
    int n;
    n=t;
    int beg,end;        //sorting
            beg=0;
            end=t-1;
    Quicksort(c,beg,end);
            Quicksort(d,beg,end);
             Quicksort(a,beg,end);
              Quicksort(b,beg,end);
            for(int i=0;i<t;i++)
            {
               // fout<<c[i]<<'\t';
            }
            //cout<<endl;
            for(int i=0;i<t;i++)
            {
                //cout<<d[i]<<'\t';
            }
            //cout<<endl;
            while(t)
            {
            //cout<<t<<endl;
                        if(a[t-1]>b[t-1])
                        {
                                     a[t-1]=b[0]=0;
                                     p1++;
                                     //cout<<100<<endl;
                        }
                        else
                        {
                        //cout<<a[t-1];
                                     a[t-1]=b[t-1]=0;
                                     //cout<<50<<endl;
                                     
                        }
                        cancel(a,t);
                        cancel(b,t);  
                        t--;
                        
            }
            //cout<<p1;
            
    
    while(n)
            {
            //cout<<n<<endl;
            if(d[0]<c[0])
                        {
                                             d[0]=c[0]=0;
                                             p2++;
                                             //cout<<100<<endl;
                                            
                        }
                         else
                        {
                                c[0]=d[n-1]=0;
                                //cout<<50<<endl;
                                
                        }
                        
                        cancel(c,n);
                        cancel(d,n);  
                        n--;
                        
            }
            cout<<p2;
            
            fout<<"Case #"<<u<<": "<<p2<<' '<<p1<<endl;
     }
            return 0;
}
