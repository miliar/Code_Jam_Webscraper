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
   aFileNameLocal = (AnsiString) "C:\\Google Test\\B-small-attempt0.txt";
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
// get c
         aTemp ="";
         for ( i = 0 ; i < 100 ; i++ )
         {
             cTemp = getc(datafile);
             if ( (AnsiString)cTemp == " " ) break;
             aTemp = aTemp + (AnsiString)cTemp;
         }
         dC[k] = aTemp.ToDouble();
// get f
         aTemp ="";
         for ( i = 0 ; i < 60000 ; i++ )
         {
             cTemp = getc(datafile);
             if ( (AnsiString)cTemp == " " ) break;
             aTemp = aTemp + (AnsiString)cTemp;
         }
         dF[k] = aTemp.ToDouble();
// get x
         aTemp ="";
         for ( i = 0 ; i < 60000 ; i++ )
         {
             cTemp = getc(datafile);
             if ( (AnsiString)cTemp == "\n" ) break;
             aTemp = aTemp + (AnsiString)cTemp;
         }
         dX[k] = aTemp.ToDouble();
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
         aTemp = AnsiString(  dTime[i]);
         aTemp = "Case #" + IntToStr(i + 1 ) + ": " +TrimLeft(aTemp.sprintf("%15.7f", dTime[i])) + "\n";

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
        dProd = 2;
        dTm = dX[i]/ dProd;
        d1 = 0;
        for ( j = 0 ; j < 50000 ; j++ )
        {
            d1 = d1 + dC[i]/ ( 2 + j * dF[i] );

            dTemp = d1 + dX[i]/ ( 2 + (j+1) * dF[i] ) ;
        
                if ( dTemp < dTm )
                {
                   dTm = dTemp;
                 }  else
                {
                 dTime[i] = dTm;
                 break;
                }
        }
   }

}
//---------------------------------------------------------------------------

