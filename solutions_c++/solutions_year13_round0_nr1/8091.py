#include<iostream>
#include<fstream>
#include<malloc.h>

using namespace std;

int gamestatus(char *line1,char *line2,char *line3,char *line4);
int hcompute(char *cases);
int vcompute(char *line1,char *line2,char *line3,char *line4);
int dcompute(char *line1,char *line2,char *line3,char *line4);

int main()
 {
   char *line1,*line2,*line3,*line4;
   char *ifilename = "c:\\A-small-attempt0.in";
   char *ofilename = "c:\\smallarge.txt";
   int return_value,count_of_testcases,i;

   line1 = (char*)malloc(sizeof(char));
   line2 = (char*)malloc(sizeof(char));
   line3 = (char*)malloc(sizeof(char));
   line4 = (char*)malloc(sizeof(char));		
  
   ifstream inputfile(ifilename);
   ofstream outputfile(ofilename);

   if(!inputfile)
     {
       cout << "There is problem in opening file" << ifilename << endl;
       return (0);
     }
   cout << "opened" << ifilename << "for reading" << endl;
   
   inputfile >> count_of_testcases;
   
   for(i=0;i<count_of_testcases;i++)
     {
         inputfile >> line1;
         inputfile >> line2;
         inputfile >> line3;
         inputfile >> line4;
         
         return_value = gamestatus(line1,line2,line3,line4);
         
         if(return_value == 1)
           {
             outputfile << "Case #" << i+1 << ":"<< " " << "X won" << "\n" << endl;
           }

         if(return_value == 2)
           {
             outputfile << "Case #" << i+1 << ":"<< " " << "O won" << "\n" << endl;
           }
           
         if(return_value == 6)
           {
             outputfile << "Case #" << i+1 << ":"<< " " << "Draw" << "\n" << endl;
           }

         if(return_value == 7)
           {
             outputfile << "Case #" << i+1 << ":"<< " " << "Game has not completed" << "\n" << endl;
           }
     } 

     outputfile.close();
     return (0);
 }

int gamestatus(char *line1,char *line2,char *line3,char *line4)
 {
   int hstatus1, hstatus2, hstatus3, hstatus4;
   int vstatus,dstatus;
   
   hstatus1 = hcompute(line1);

   if(hstatus1 == 1 || hstatus1 == 2)
     {
       return (hstatus1);
     }
   else
     {
       hstatus2 = hcompute(line2);
     } 
     
   if(hstatus2 == 1 || hstatus2 == 2)
     {
       return (hstatus2);
     }
   else
     {
       hstatus3 = hcompute(line3);
     } 

   if(hstatus3 == 1 || hstatus3 == 2)
     {
       return (hstatus3);
     }
   else
     {
       hstatus4 = hcompute(line4);
     } 

   if(hstatus4 == 1 || hstatus4 == 2)
     {
       return (hstatus4);
     }
   else
     {
       //if(hstatus1 == 7 && hstatus2 == 7 && hstatus3 == 7 && hstatus4 == 7)
      // return(7);
      // else
       vstatus = vcompute(line1,line2,line3,line4);
	   if (vstatus == 1 || vstatus ==2)
	     {
			 return(vstatus);
	     }
	   else
	    {
			dstatus = dcompute(line1,line2,line3,line4);
			if(dstatus == 1 || dstatus == 2)
			  {
			    return(dstatus);
			  }  
			if(hstatus1 == 7 && hstatus2 == 7 && hstatus3 == 7 && hstatus4 == 7)
              return(7);
			else
				return(6);


	    }
     } 
     
 }


int hcompute(char *cases)
{
  int i;
  int x=0,t=0,o=0;
  
  for(i=0;i<4;i++)
  {
    if(cases[i] == 'X')
     {
       x++;
     }
    if(cases[i] == 'O')
     {
       o++;
     }
    if(cases[i] == 'T')
     {
       t++;
     }
    if(cases[i] == '.')
     {
       return(7);
     }
    
  }

  if(x == 4 || (x == 3 && t == 1) )
    return(1);

  if(o == 4 || (o == 3 && t == 1) )
    return(2);
  else
    return(6);
}

int vcompute(char *line1,char *line2,char *line3,char *line4)
{
  int i=0;
  int x=0,t=0,o=0;
 for(i=0;i<4;i++)
 {
   if (line1[i] == 'X' && line2[i] == 'X' && line3[i] == 'X' && line4[i] == 'X')
        {
		  return(1);
        }
      
  if (line1[i] == 'O' && line2[i] == 'O' && line3[i] == 'O' && line4[i] == 'O')
        {
			return(2);
        }
  if(line1[i] == 't' || line2[i] == 't' || line3[i] == 't' || line4[i] == 't')
  {
	  t = 1;
	  if(line1[i] == 'X')
		  x++;
	  if(line2[i] == 'X')
		  x++;
	  if(line3[i] == 'X')
		  x++;
	  if(line4[i] == 'X' )
		  x++;
	  if(x == 3 && t == 1)
		  return(1);

	  if(line1[i] == 'O')
		  o++;
	  if(line2[i] == 'O')
		  o++;
	  if(line3[i] == 'O')
		  o++;
	  if(line4[i] == 'O' )
		  o++;
	  if(o == 3 && t == 1)
		  return(2);
	  else
		  return(6);
  }

 }
 // if(x == 4 || (x == 3 && t == 1) )
   // return(1);

//  if(o == 4 || (o == 3 && t == 1) )
  //  return(2);
  //else
    //return(6);
}

int dcompute(char *line1,char *line2,char *line3,char *line4)
{

	int i=0;
	int x=0,t=0,o=0;

	if(line1[i] == 'X' && line2[i+1] == 'X' && line3[i+2] == 'X' && line4[i+3] == 'X' )
		return(1);

    if(line1[i+3] == 'X' && line2[i+2] == 'X' && line3[i+1] == 'X' && line4[i] == 'X' )
		return(1);

    if(line1[i] == 'O' && line2[i+1] == 'O' && line3[i+2] == 'O' && line4[i+3] == 'O' )
		return(2);

    if(line1[i+3] == 'O' && line2[i+2] == 'O' && line3[i+1] == 'O' && line4[i] == 'O' )
		return(2);

    if(line1[0] == 'X')
		x++;
	if(line1[0] == 'O')
		o++;
	if(line1[0] == 'T')
		t++;

	if(line2[1] == 'X')
		x++;
	if(line2[1] == 'O')
		o++;
	if(line2[1] == 'T')
		t++;

	if(line3[2] == 'X')
		x++;
	if(line3[2] == 'O')
		o++;
	if(line3[2] == 'T')
		t++;

	if(line4[3] == 'X')
		x++;
	if(line4[3] == 'O')
		o++;
	if(line4[3] == 'T')
		t++;

	if(x == 3 && t == 1)
		return(1);
	if(o == 3 && t == 1)
		return(2);

	x=0;
	t=0;
	o=0;

	if(line1[3] == 'X')
		x++;
	if(line1[3] == 'O')
		o++;
	if(line1[3] == 'T')
		t++;

	if(line2[2] == 'X')
		x++;
	if(line2[2] == 'O')
		o++;
	if(line2[2] == 'T')
		t++;

	if(line3[1] == 'X')
		x++;
	if(line3[1] == 'O')
		o++;
	if(line3[1] == 'T')
		t++;

	if(line4[0] == 'X')
		x++;
	if(line4[0] == 'O')
		o++;
	if(line4[0] == 'T')
		t++;

	if(x == 3 && t == 1)
		return(1);
	if(o == 3 && t == 1)
		return(2);
	else
	  return(6);

	
}    