void CDlgGoogleCodeJam::QR2013ProblemC(CStdioFile *pInputFile, CStdioFile *pOutputFile)
{
	int				i, k, iCount, iSize;
	__int64		j, l, T, A, B, iPower, A1, B1;
	CString		sReadText, sWriteText, sTempText, sNumber, sRevNumber;
	CString		sNum;
	bool			bStop;

	pInputFile->ReadString(sReadText);
	//AfxMessageBox(sReadText);
	T = atoi(sReadText);
	for (i = 1; i <= T; i++)
	{
		pInputFile->ReadString(sReadText);
		sscanf(sReadText,"%I64d %I64d", &A, &B);

		A1 = ceil(sqrt(A));
		B1 = sqrt(B);

		iCount = 0;
		for (j=A1; j<=B1; j++)
		{
			bStop = false;

			if (j >= 10)
			{
				l = j;
				while (l > 0)
				{
					if (l%10 > 3)
					{
						bStop = true;
						break;
					}
					l = l/10;
				}
			}
			else
				if (j > 3)
					bStop = true;

			if (bStop)
				continue;

			if (j%10 == 0)
				continue;

			sNum.Format("%I64d", j);
			iSize = sNum.GetLength();
			for (k=0; k<iSize/2; k++)
				if (sNum[k] != sNum[iSize-k-1])
				{
					bStop = true;
					break;
				}

			if (bStop)
				continue;

			iPower = pow(j, 2);

			sNum.Format("%I64d", iPower);
			iSize = sNum.GetLength();
			for (k=0; k<iSize/2; k++)
				if (sNum[k] != sNum[iSize-k-1])
				{
					bStop = true;
					break;
				}

			if (bStop)
				continue;

			iCount++;
		}

		//sTempText.Format("%I64d", iCount);

		// Print result
		sWriteText.Format("Case #%d: %d\n", i, iCount);
		pOutputFile->WriteString(sWriteText);
	}
}