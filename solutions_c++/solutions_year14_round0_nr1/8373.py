#include <iostream>
#include <fstream>
#include <string>
#include <sstream>


using namespace std;


int main()
{
    string line;
    string row;
    int case_no;
    int case_total;
    int m[4];
    int k[4];
    
    ifstream myfile ("Input.txt");
    ofstream outfile ("Output.txt");
    outfile.is_open();
    if (myfile.is_open())
    {
     getline (myfile,line);
     case_total = atoi( line.c_str());
     //cout<<case_total<<endl;
     for(int i=0;i<case_total;i++)
     {
             outfile<<"Case #"<<i+1<<": ";
             for(int j=0;j<2;j++)
             {
                     getline (myfile,line);
                     case_no = atoi( line.c_str());
                     //cout<<case_no<<endl;
                     for(int f=0;f<4;f++)
                     {
                      getline (myfile,line);
                              if((f+1)==case_no)
                               {
                               row=line;
                               //cout<<row<<endl;
                               }
                     }
                     
                     stringstream stream(row);
                     
                     for(int l=0;l<4;l++)
                     {
                     int n;
                     stream>>n;
                     m[l]=n;
                     //cout<<m[l]<<endl;
                     }
                     
                     if (j==0)
                     {
                     for(int l=0;l<4;l++)
                     k[l]=m[l];
                     }
                     
                     

                     
                     
                     
                     
             }
             
           /*  for(int l=0;l<4;l++)
             cout<<k[l]<<" ";
             cout<<endl;
             for(int l=0;l<4;l++)
             cout<<m[l]<<" ";
             cout<<endl;
             */
             int count =0;
             int no=0;
             for(int c=0;c<4;c++)
             {
                     for(int d=0;d<4;d++)
                     {
                             if(k[c] == m[d])
                             {
                             count++;
                             no=k[c];
                             
                             }
                     }
             }
             
             //if (outfile.is_open())
             //{
             if (count == 0)
             outfile<<"Volunteer cheated!"<<endl;
             else if(count > 1)
             outfile<<"Bad magician!"<<endl;
             else
             outfile<<no<<endl;
             //}
             //else cout << "file"; 
             
             
             
             
             
     }      
          myfile.close();
          outfile.close();   
     }

  else cout << "Unable to open file"; 

    system("pause");
    return 0;
}
