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
   
}
//---------------------------------------------------------------------------

void __fastcall TForm1::Button1Click(TObject *Sender)
{
   int i,j,k,d,m,p,r,s,t;   AnsiString aFileNameLocal; char* cFileNameLocal;
   cFileNameLocal = new char [150];  AnsiString aTemp;  char cTemp;

   FILE *datafile;
//  set up the path and file name
   aFileNameLocal = (AnsiString) "C:\\Users\\thinus\\downloads\\D-small-attempt1.in";
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
      for ( i = 0 ; i < 100 ; i++ )
      {
         cTemp = getc(datafile);
         if ( (AnsiString)cTemp == "\n" ) break;
         aTemp = aTemp + (AnsiString)cTemp;
      }
      iT = StrToInt ( aTemp);
// get all cases
      for ( k = 0 ; k < iT ; k++)
      {
// get X
         aTemp ="";
         for ( i = 0 ; i < 100 ; i++ )
         {
             cTemp = getc(datafile);
             if ( (AnsiString)cTemp == " " ) break;
             aTemp = aTemp + (AnsiString)cTemp;
         }
         iX[k] = aTemp.ToInt();
// get R
         aTemp ="";
         for ( i = 0 ; i < 60000 ; i++ )
         {
             cTemp = getc(datafile);
             if ( (AnsiString)cTemp == " " ) break;
             aTemp = aTemp + (AnsiString)cTemp;
         }
         iR[k] = aTemp.ToDouble();
// get C
         aTemp ="";
         for ( i = 0 ; i < 60000 ; i++ )
         {
             cTemp = getc(datafile);
             if ( (AnsiString)cTemp == "\n" ) break;
             aTemp = aTemp + (AnsiString)cTemp;
         }
         iC[k] = aTemp.ToInt();
         aTemp = aTemp;
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
      for ( i = 0 ; i < iT ; i++ )
      {
         aTemp = "Case #" + IntToStr(i + 1 ) + ": " + aAnswer[i] + "\n";

         StrPCopy(cTemp, aTemp);
         fwrite ( cTemp, 1, aTemp.Length(), datafile );
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
   double dTm, dTemp, d1, d2, dProd;
//
   for ( i = 0; i < iT ; i++ )
   {
        if ( iX[i] == 1 ){
            aAnswer[i] = "Gabriel";
        }else{
            if ( iX[i] > 6 ) {
                aAnswer[i] = "Richard";
            }else{
                if ( (iR[i] * iC[i]) % iX[i] > 0 ) {
                    aAnswer[i] = "Richard";
                }else{
                    if ( iR[i] * iC[i] >= iX[i] * ( iX[i] - 1 )){
                       aAnswer[i] = "Gabriel";
                    }else{
                        if ( iR[i] < iX[i] || iC[i] < iX[i] ){
                           aAnswer[i] = "Richard";
                        }else{
                            if ( iR[i] < (iX[i]/2) || iC[i] < (iX[i]/2) ){
                               aAnswer[i] = "Richard";
                            }else{
                                aAnswer[i] = "Gabriel";
                            }
                        }
                    }
                }
            }
        }
   }
}
//---------------------------------------------------------------------------

