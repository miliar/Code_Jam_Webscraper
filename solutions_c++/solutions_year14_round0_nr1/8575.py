//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop

#include "Unit1.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.dfm"
TForm1 *Form1;
//---------------------------------------------------------------------------
__fastcall TForm1::TForm1(TComponent* Owner)
   : TForm(Owner)
{
   iNumber = 1;
}
//---------------------------------------------------------------------------

void __fastcall TForm1::Button1Click(TObject *Sender)
{
   int i,j,k,d,m,p,r,s,t;   AnsiString aFileNameLocal; char* cFileNameLocal;
   cFileNameLocal = new char [150];  AnsiString aTemp;  char cTemp;

   FILE *datafile;
//  set up the path and file name
   aFileNameLocal = (AnsiString) "C:\\Google Test\\test.txt";
   StrPCopy( cFileNameLocal, aFileNameLocal );
// import the data
   if ( ( datafile = fopen(cFileNameLocal,"r+") ) == NULL )
   {
      MessageBox(0, " Cannot open the data file", "Error Message  1" , 0 );
      delete [] cFileNameLocal;
      return;
   }
   else
   {
// get the data file
//
// get number of cases
      aTemp ="";
      for ( i = 0 ; i < 1000 ; i++ )
      {
         cTemp = getc(datafile);
         if ( (AnsiString)cTemp == "\n" ) break;
         aTemp = aTemp + (AnsiString)cTemp;
      }
      iT = StrToInt ( aTemp);
// get all cases
      for ( k = 0 ; k < iT ; k++)
      {
// get number of lines
         aTemp ="";
         for ( i = 0 ; i < 1000 ; i++ )
         {
            cTemp = getc(datafile);
            if ( (AnsiString)cTemp == " " ) break;
            aTemp = aTemp + (AnsiString)cTemp;
         }
         iN[k] = StrToInt ( aTemp);
// get number of columns
         aTemp ="";
         for ( i = 0 ; i < 1000 ; i++ )
         {
            cTemp = getc(datafile);
            if ( (AnsiString)cTemp == "\n" ) break;
            aTemp = aTemp + (AnsiString)cTemp;
         }
         iM[k] = StrToInt ( aTemp);

// get matrix of heights
         for ( r = 0 ; r < iN[k] ; r++ )
         {
            for ( s = 0 ; s < iM[k] ; s++ )
            {
               aTemp ="";
               for ( i = 0 ; i < 60000 ; i++ )
               {
                  cTemp = getc(datafile);
                  if ( (AnsiString)cTemp == " " || (AnsiString)cTemp == "\n"  ) break;
                  aTemp = aTemp + (AnsiString)cTemp;
               }
               iMatrix[k][r][s] = StrToInt ( aTemp);
            }
         }
      }
    }
//
   fclose (datafile);
   delete [] cFileNameLocal;
}
//---------------------------------------------------------------------------
// create output file
void __fastcall TForm1::Button2Click(TObject *Sender)
{
   int i,j,k,d,m,p;   AnsiString aFileNameLocal; char* cFileNameLocal;
   cFileNameLocal = new char [150];  AnsiString aTemp;  char* cTemp;
   int iB[10000]; int iD[10000]; int iF[10000];
   FILE *datafile;               cTemp = new char [150];
//  set up the path and file name
   aFileNameLocal = (AnsiString) "C:\\Google Test\\output.txt";
   StrPCopy( cFileNameLocal, aFileNameLocal );
// set up the data
   if ( ( datafile = fopen(cFileNameLocal,"w+") ) == NULL )
   {
      MessageBox(0, " Cannot open the data file", "Error Message  1" , 0 );
      delete [] cFileNameLocal;
      return;
   }
   else
   {
// write the output file
      for ( i = 1 ; i <= iT ; i++ )
      {
         if ( iAns[i - 1 ] == 0 )
         {
            aAnswers[i] = "Case #" + IntToStr(i) + ": " + "YES" + "\n";
         }
         else
         {
            aAnswers[i] = "Case #" + IntToStr(i) + ": " + "NO" + "\n";
         }
         StrPCopy(cTemp, aAnswers[i]);
         fwrite ( cTemp, 1, aAnswers[i].Length(), datafile );
      }   
   } 
   fclose (datafile);
   delete [] cFileNameLocal;
}
//---------------------------------------------------------------------------
//
void __fastcall TForm1::Button3Click(TObject *Sender)
{
   int i,j,k,l,m,n,p,s,t,u,v;    AnsiString aTemp;   int iFreq;  int iFir;   int iSec;
   int iCount[150];  int iSelect;         int iRow;     int iCol;       int iInvalid;
//
   for ( i = 0; i < iT ; i++ )
   {
//   find row max

       for ( j = 0 ; j < iN[i] ; j++ )
       {
          iRow = 0 ;
          for ( k = 0 ; k < iM[i] ; k++ )
          {
             if ( iMatrix[i][j][k] > iRow ) iRow = iMatrix[i][j][k];
          }
          iRowMax[i][j] = iRow ;
       }

//   find col max

       for ( j = 0 ; j < iM[i] ; j++ )
       {
          iCol = 0 ;
          for ( k = 0 ; k < iN[i] ; k++ )
          {
             if ( iMatrix[i][k][j] > iCol ) iCol = iMatrix[i][k][j];
          }
          iColMax[i][j] = iCol ;
       }

//   check matrix
       iInvalid = 0 ;
       for ( j = 0 ; j < iM[i] ; j++ )
       {
          for ( k = 0 ; k < iN[i] ; k++ )
          {
             if ( iMatrix[i][k][j] < iColMax[i][j] &&
                      iMatrix[i][k][j] < iRowMax[i][k] )
             {
                iInvalid++;
             }
          }
       }
       iAns[i] = 0 ;
       if ( iInvalid > 0 ) iAns[i] = 1;
   }
}
//---------------------------------------------------------------------------

